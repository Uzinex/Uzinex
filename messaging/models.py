from django.db import models
from django.conf import settings
from marketplace.models import Project


class Thread(models.Model):
    project = models.ForeignKey(Project, related_name='threads', on_delete=models.CASCADE)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='threads')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Thread for {self.project_id}"


class Message(models.Model):
    thread = models.ForeignKey(Thread, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Message {self.id}"
