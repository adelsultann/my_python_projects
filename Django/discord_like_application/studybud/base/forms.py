from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # to greate all the fields in the Room models
        fields = "__all__"
        exclude = ['host','participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", 'email']