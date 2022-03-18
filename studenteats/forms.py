from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password','email',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name','website', 'telephone','university','location','picture',)
"""
class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50, required=False)
    last_name = forms.CharField(label="Last Name", max_length=50, required=False)
    email = forms.CharField(label="Email", max_length=50, required=False)
    telephone = forms.CharField(label="Telephone", max_length=50, required=False)
    birthday = forms.CharField(label="Birthday", max_length=50, required=False)
    university = forms.CharField(label="University", max_length=50, required=False)
    location = forms.CharField(label="Location", max_length=50, required=False)

class SignupForm(forms.Form):

    def signup(self, request, user):
        user_profile = UserProfile()
        user_profile.user=user
        user.save()
        user_profile.save()
"""

