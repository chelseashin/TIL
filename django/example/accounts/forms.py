from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class UserCustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['email']
        