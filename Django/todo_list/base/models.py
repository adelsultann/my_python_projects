from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # User model take care of user name and email, password
    #user here is one to many relationship one user can have alot of task
    # on_delete means if the user was deleted by admin or by itself what we should do with the data
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # True or False | default means when the item created we will set it as False not complete
    # it will be shown as check mark
    complete = models.BooleanField(default=False)
    # auto_now_add create the date automatically
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
# Create your models here.
