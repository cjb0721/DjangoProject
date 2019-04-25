from django.forms import ModelForm
from .models import *


class Form(ModelForm):
    class Meta():
        model = Comments
        fields = ['name', 'email', 'url', 'text']



