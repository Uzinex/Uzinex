from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "skills",
            "budget_min",
            "budget_max",
            "deadline",
            "status",
        ]

    def clean(self):
        cleaned = super().clean()
        min_budget = cleaned.get("budget_min")
        max_budget = cleaned.get("budget_max")
        if min_budget is not None and max_budget is not None and min_budget > max_budget:
            raise forms.ValidationError("Minimum budget cannot exceed maximum budget")
        skills = cleaned.get("skills")
        if isinstance(skills, str):
            cleaned["skills"] = [s.strip() for s in skills.split(',') if s.strip()]
        return cleaned
