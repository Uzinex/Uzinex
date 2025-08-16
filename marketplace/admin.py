from django.contrib import admin
from .models import Project, Proposal, Contract


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "client", "status", "created_at")
    list_filter = ("status",)


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "freelancer", "status", "created_at")
    list_filter = ("status",)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "proposal", "status", "started_at")
    list_filter = ("status",)
