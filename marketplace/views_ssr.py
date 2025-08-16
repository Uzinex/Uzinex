from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Project
from .forms import ProjectForm


class ProjectsListView(ListView):
    model = Project
    template_name = "pages/marketplace/projects_list.html"
    paginate_by = 10

    def get_queryset(self):
        qs = Project.objects.all().order_by("-created_at")
        status = self.request.GET.get("status")
        if status:
            qs = qs.filter(status=status)
        skill = self.request.GET.get("skill")
        if skill:
            skills = [s.strip() for s in skill.split(",") if s.strip()]
            qs = qs.filter(skills__contains=skills)
        budget_min = self.request.GET.get("budget_min")
        budget_max = self.request.GET.get("budget_max")
        if budget_min:
            qs = qs.filter(budget_min__gte=budget_min)
        if budget_max:
            qs = qs.filter(budget_max__lte=budget_max)
        return qs


class ProjectDetailView(DetailView):
    model = Project
    template_name = "pages/marketplace/project_detail.html"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "pages/marketplace/project_create.html"
    success_url = reverse_lazy("projects_list")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.role != "client":
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)
