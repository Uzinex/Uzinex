from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from .models import Thread, Message
from .forms import MessageForm


class ThreadListView(LoginRequiredMixin, ListView):
    model = Thread
    template_name = "pages/messaging/thread_list.html"

    def get_queryset(self):
        return self.request.user.threads.all()


class ThreadDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Thread
    form_class = MessageForm
    template_name = "pages/messaging/thread_detail.html"

    def get_success_url(self):
        return reverse_lazy("thread_detail", args=[self.kwargs["pk"]])

    def dispatch(self, request, *args, **kwargs):
        thread = self.get_object()
        if request.user not in thread.participants.all():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        Message.objects.create(
            thread=self.get_object(),
            sender=self.request.user,
            body=form.cleaned_data["body"],
        )
        return redirect(self.get_success_url())
