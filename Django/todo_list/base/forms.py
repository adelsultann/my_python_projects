from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        # to greate all the fields in the Room models
        fields = "__all__"
        exclude = ['user']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']