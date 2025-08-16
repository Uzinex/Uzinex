from django.db import models
from django.conf import settings


class Project(models.Model):
    STATUS_CHOICES = [
        ("open", "open"),
        ("in_progress", "in_progress"),
        ("completed", "completed"),
    ]
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.JSONField(default=list, blank=True)
    budget_min = models.DecimalField(max_digits=10, decimal_places=2)
    budget_max = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Proposal(models.Model):
    STATUS_CHOICES = [
        ("pending", "pending"),
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]
    project = models.ForeignKey(Project, related_name="proposals", on_delete=models.CASCADE)
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="proposals", on_delete=models.CASCADE)
    cover_letter = models.TextField()
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    eta_days = models.PositiveIntegerField(default=7)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Proposal by {self.freelancer}"


class Contract(models.Model):
    STATUS_CHOICES = [
        ("active", "active"),
        ("closed", "closed"),
    ]
    project = models.OneToOneField(Project, related_name="contract", on_delete=models.CASCADE)
    proposal = models.OneToOneField(Proposal, related_name="contract", on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    def __str__(self) -> str:
        return f"Contract for {self.project}"
