from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        user = authenticate(
            username=cleaned.get("username"), password=cleaned.get("password")
        )
        if not user:
            raise forms.ValidationError("Invalid credentials")
        cleaned["user"] = user
        return cleaned


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password", "role"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    skills = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ["bio", "skills", "hourly_rate", "avatar"]

    def clean_skills(self):
        data = self.cleaned_data.get("skills", "")
        if not data:
            return []
        if isinstance(data, list):
            return data
        lines = [s.strip() for s in data.splitlines() if s.strip()]
        return lines

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.skills = self.cleaned_data.get("skills", [])
        if commit:
            profile.save()
        return profile
