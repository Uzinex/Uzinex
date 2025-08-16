from django.views.generic import TemplateView
from marketplace.models import Project


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_projects"] = Project.objects.order_by("-created_at")[:5]
        return context

