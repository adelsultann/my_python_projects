from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Room, Topic, User, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RoomForm, UserForm


# tutorial database

# rooms = [
#     {'id': 1, 'name': 'lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'frontend developers'}
# ]


# Create your views here.

def loginPage(request):
    page = "login"
    # if user is_authenticated we will not allow him to go to the log in page
    if request.user.is_authenticated:
        return redirect("Home")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist.')
            # if user exist authenticate it and register the login for the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # this method will register the user to the database | check the browser inspect--> storage--> cookies
            login(request, user)
            return redirect("Home")
        else:
            messages.error(request, 'Username or password incorrect.')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('Home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # if you want to get the user object we have to add commit=False| so we can make it lower case instead
            # and allow the user login with lower or upper case
            # method to save the form to the database
            # we will not save the room directly first we will find out the participant then we will save the room in
            # the database
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # after saving the information we will login the user
            login(request, user)
            return redirect("Home")
        else:
            messages.error(request, "an Error occurred during registration")

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ''
    # icontains | to search for any letter that contain in q variable i for case capital sensitive
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topic = Topic.objects.all()[0:5] # this is the topics in the right page we only render the last 5 instead of all
    # to get the count of the room in database
    room_count = rooms.count()
    # filter عشان لو بحث باستخدام المواضيع اللي ع اليسار يطلع له الفيد برضو في الاكتفيتي
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    context = {'rooms': rooms, 'topics': topic, 'room_count': room_count, 'room_messages': room_messages}

    return render(request, "base/home.html", context)


def room(request, pk):
    # pk primary key
    room = Room.objects.get(id=pk)
    # get all the childern--> comments of the room
    # we can query child object of specific room | the parent model is the Room
    # we write the child with lower case
    # ordering accordion to the newest
    room_messages = room.message_set.all()  # .order_by('-created')
    # we query the many to many by all | but one to many by set_all as shown above
    participants = room.participants.all

    if request.method == "POST":
        # create a new message in the database
        messages = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body")
        )
        # to add the user to the participants
        room.participants.add(request.user)
        # it's ok to not write the code below | but we need it to refresh the page and to not miss up some functionality
        return redirect("Room", pk=room.id)

    context = {
        'room': room,
        'room_messages': room_messages,
        "participants": participants
    }
    return render(request, "base/room.html", context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    # to get all the children of specific object
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        # get_or_create | to create a new table in the database or get it if exixt
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )

        return redirect("Home")

    context = {'form': form, 'topics': topics}
    return render(request, "base/room_form.html", context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    # if the user is the owner of the room
    if request.user != room.host:
        return HttpResponse("You are not allowed here ")
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        # get_or_create | to create a new table in the database or get it if exixt
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()

        return redirect("Home")

    context = {"form": form, 'topics': topics, 'room': room}
    return render(request, "base/room_form.html", context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    # if the user is the owner of the room
    if request.user != room.host:
        return HttpResponse("You are not allowed here ")
    if request.method == "POST":
        room.delete()
        return redirect("Home")
    return render(request, "base/delete.html", {'obj': room})


@login_required(login_url='login')
def deleteMessage(request, pk):
    user_message = Message.objects.get(id=pk)
    # if the user is the owner of the room
    if request.user != user_message.user:
        return HttpResponse("You are not allowed here ")
    if request.method == "POST":
        user_message.delete()
        return redirect("Home")
    return render(request, "base/delete.html", {'obj': user_message})


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})


def topicPage(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ''

    # لو ماحطست فلتر معين وخليت القوسين فاضيه بيطلع لك كل النتايج
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics':topics})


def activityPage(request):
    room_messages = Message.objects.all()

    return render(request, 'base/activity.html', {'room_messages': room_messages})