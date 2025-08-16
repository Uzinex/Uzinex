from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Thread, Message
from .serializers import ThreadSerializer, MessageSerializer


class ThreadViewSet(viewsets.ModelViewSet):
    """Chat threads between client and freelancer for a project."""
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all().select_related('project').prefetch_related('participants')
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(participants=self.request.user)

    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if not project.contract:
            raise PermissionDenied('Project has no contract')
        freelancer = project.contract.proposal.freelancer
        if self.request.user not in [project.client, freelancer]:
            raise PermissionDenied('Not a participant')
        thread = serializer.save()
        thread.participants.set([project.client, freelancer])


class MessageViewSet(viewsets.ModelViewSet):
    """Messages inside a thread."""
    serializer_class = MessageSerializer
    queryset = Message.objects.all().select_related('thread', 'sender', 'thread__project')
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(thread__participants=self.request.user)

    def perform_create(self, serializer):
        thread = serializer.validated_data['thread']
        if self.request.user not in thread.participants.all():
            raise PermissionDenied('Not a participant')
        serializer.save(sender=self.request.user)
