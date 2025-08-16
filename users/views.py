from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.template.loader import render_to_string
from .models import User
from .serializers import UserSerializer, RegisterSerializer, ProfileSerializer
from .forms import LoginForm, RegisterForm, ProfileForm


class RegisterAPIView(APIView):
    """Register a new user."""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class MeAPIView(generics.RetrieveAPIView):
    """Return current authenticated user with profile."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ProfileUpdateAPIView(generics.UpdateAPIView):
    """Update current user's profile."""
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


# SSR views


class LoginView(FormView):
    template_name = "pages/auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        auth.login(self.request, form.cleaned_data["user"])
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = "pages/auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        auth.login(self.request, user)
        template = (
            "emails/welcome_client.html"
            if user.role == "client"
            else "emails/welcome_freelancer.html"
        )
        render_to_string(template, {"user": user})
        messages.success(self.request, "Registration successful")
        return super().form_valid(form)


def logout_view(request):
    auth.logout(request)
    messages.info(request, "Logged out")
    return redirect("home")


class MeView(LoginRequiredMixin, TemplateView):
    template_name = "pages/users/me.html"


class ProfileEditView(LoginRequiredMixin, FormView):
    template_name = "pages/users/profile_edit.html"
    form_class = ProfileForm
    success_url = reverse_lazy("me")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.user.profile
        initial = kwargs.get("initial", {})
        initial["skills"] = "\n".join(self.request.user.profile.skills)
        kwargs["initial"] = initial
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Profile updated")
        return super().form_valid(form)
