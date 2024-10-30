from django.forms import ModelForm
from .models import *


class DashboardForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'profile_pic', 'email']