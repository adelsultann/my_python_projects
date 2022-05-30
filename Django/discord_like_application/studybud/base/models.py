from django.db import models
from django.contrib.auth.models import User


# to create database run this command in terminal | python mange.py migrate
# after you create the module run this command to initiate the table | python mange.py makemigrations
# after that run again | python mange.py migrate


# Create your models here.
# create a database

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # on_delete=models.SET_NULL | means when topic deleted we don't delete the room
    # that's tells Django each room is related to single room
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # null = True means it can be empty
    description = models.TextField(null=True, blank=True)
    # many to many relation
    # | we can't put User only because we have one above so we put an extra references related_name
    # blank = True | means you can submit a form without writing anything in this fields
    participants = models.ManyToManyField(User,related_name='participants',blank=True)

    # everytime the save method call we will save the time in this table
    # auto_now fields are updated to the current timestamp every time an object is saved
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add field is saved as the current timestamp when a
    # row is first added to the database and is therefore perfect for tracking when it was created.
    created = models.DateTimeField(auto_now_add=True)

    # to return the newest Room in order
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    # User relationship is one to many | it means user can have many messages but massage can have only one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # CASCADE to delete all the database once the parent deleted
    # room relationship is one to many | it means room can have many messages
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        # to display only the first 50 characters
        return self.body[0:50]
