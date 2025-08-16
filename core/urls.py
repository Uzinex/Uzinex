from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from core.views import HomeView
from users.views import LoginView, RegisterView, MeView, ProfileEditView, logout_view
from marketplace.views_ssr import (
    ProjectsListView,
    ProjectDetailView,
    ProjectCreateView,
)
from messaging.views_ssr import ThreadListView, ThreadDetailView


urlpatterns = [
    path("admin/", admin.site.urls),

    # SSR pages
    path("", HomeView.as_view(), name="home"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/logout/", logout_view, name="logout"),

    path("me/", MeView.as_view(), name="me"),
    path("me/edit/", ProfileEditView.as_view(), name="profile_edit"),

    path("projects/", ProjectsListView.as_view(), name="projects_list"),
    path("projects/new/", ProjectCreateView.as_view(), name="project_create"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),

    path("threads/", ThreadListView.as_view(), name="thread_list"),
    path("threads/<int:pk>/", ThreadDetailView.as_view(), name="thread_detail"),

    # API
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/auth/", include("users.urls")),
    path("api/marketplace/", include("marketplace.urls")),
    path("api/messaging/", include("messaging.urls")),
    path("api/payments/", include("payments.urls")),
]
