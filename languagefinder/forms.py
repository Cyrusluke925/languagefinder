from django import forms
from languageit.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class ProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
