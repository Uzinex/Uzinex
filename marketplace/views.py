from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from .models import Project, Proposal, Contract
from .serializers import ProjectSerializer, ProposalSerializer, ContractSerializer


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client'


class IsFreelancer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'freelancer'


class IsProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.client == request.user


class IsProposalAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.freelancer == request.user


class ProjectViewSet(viewsets.ModelViewSet):
    """CRUD for client projects with filtering and ordering."""
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().select_related('client')

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsClient()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsProjectOwner()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params
        status_val = params.get('status')
        if status_val:
            qs = qs.filter(status=status_val)
        skills = params.getlist('skill')
        if skills:
            qs = qs.filter(skills__overlap=skills)
        budget_min = params.get('budget_min')
        if budget_min:
            qs = qs.filter(budget_min__gte=budget_min)
        budget_max = params.get('budget_max')
        if budget_max:
            qs = qs.filter(budget_max__lte=budget_max)
        deadline_before = params.get('deadline_before')
        if deadline_before:
            qs = qs.filter(deadline__lte=deadline_before)
        deadline_after = params.get('deadline_after')
        if deadline_after:
            qs = qs.filter(deadline__gte=deadline_after)
        ordering = params.get('ordering')
        if ordering in ['created_at', '-created_at', 'budget_min', 'budget_max', 'deadline', '-deadline', '-budget_min', '-budget_max']:
            qs = qs.order_by(ordering)
        return qs


class ProposalViewSet(viewsets.ModelViewSet):
    """Manage proposals from freelancers."""
    serializer_class = ProposalSerializer
    queryset = Proposal.objects.all().select_related('project', 'freelancer')

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsFreelancer()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsProposalAuthor()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if not user.is_authenticated:
            return qs.none()
        return qs.filter(Q(project__client=user) | Q(freelancer=user))

    def perform_create(self, serializer):
        if self.request.user.role != 'freelancer':
            raise PermissionDenied('Only freelancers can create proposals')
        serializer.save(freelancer=self.request.user)


class ContractViewSet(viewsets.ModelViewSet):
    """Create and view contracts between client and freelancer."""
    serializer_class = ContractSerializer
    queryset = Contract.objects.all().select_related('project', 'proposal', 'proposal__freelancer', 'project__client')

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsClient()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if not user.is_authenticated:
            return qs.none()
        return qs.filter(Q(project__client=user) | Q(proposal__freelancer=user))

    def perform_create(self, serializer):
        proposal = serializer.validated_data['proposal']
        project = proposal.project
        if project.client != self.request.user:
            raise PermissionDenied('Not your project')
        if project.contract:
            raise PermissionDenied('Contract already exists')
        serializer.save(project=project)
        project.status = 'in_progress'
        project.save(update_fields=['status'])
        proposal.status = 'accepted'
        proposal.save(update_fields=['status'])
        Proposal.objects.filter(project=project).exclude(id=proposal.id).update(status='rejected')
