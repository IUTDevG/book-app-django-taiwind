from django.forms import forms
from .models import CustomUser


class CustomUserForm(forms.Form):
    model = CustomUser
    fields =   ['email', 'first_name', 'last_name','password']
    