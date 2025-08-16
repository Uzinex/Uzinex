from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    ROLE_CHOICES = [
        ("client", "Client"),
        ("freelancer", "Freelancer"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="client")


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    skills = models.JSONField(default=list, blank=True)
    hourly_rate = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    avatar = models.URLField(blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Profile of {self.user.username}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
