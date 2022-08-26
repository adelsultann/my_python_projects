from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.


def registerPage(request):
    page = "register"
    # form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    context = {'form': form,
               'page': page}
    return render(request, 'base/signup.html', context)


def LoginUser(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist.')
            user = authenticate(request, username=username, password=password)

        if user is not None:
            # this method will register the user to the database | check the browser inspect--> storage--> cookies
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Username or password incorrect.')
    context = {'page': page}
    return render(request, 'base/signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def home(request):
    incomplete_task = Task.objects.filter(user=request.user, complete=False).count()
    tasks = Task.objects.all()

    # else '' because if there is no search leave it empty
    q = request.GET.get("q") if request.GET.get("q") != None else ''
    if q:
        tasks = Task.objects.filter(title__icontains=q)

    # q = عشان لو بحثنا شي وضغطنا انتر مايختفي من خانه البحث
    context = {
        'tasks': tasks,
        'q': q,
        'incomplete_task': incomplete_task

    }

    return render(request, "base/home.html", context)


@login_required(login_url='login')
def task_details(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'task': task
    }
    return render(request, "base/task.html", context)


#
# class TaskDetail(DetailView):
#     model = Task
#     context_object_name = 'task'
#     template_name = 'base/task.html'

@login_required(login_url='login')
def Task_create(request):
    form = TaskForm()
    if request.method == "POST":
        Task.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            complete=request.POST.get('complete') == 'on'

        )

        return redirect("home")

    context = {'form': form}
    return render(request, "base/task_form.html", context)


@login_required(login_url='login')
def Task_update(request, pk):
    task = Task.objects.get(id=pk)
    task_complete = task.complete = True

    # instance | to auto fill the form
    form = TaskForm(instance=task)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.complete = request.POST.get('complete') == 'on'

        task.save()

        return redirect("home")

    context = {"form": form, 'task': task, }
    return render(request, "base/task_form.html", context)


@login_required(login_url='login')
def Delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    return render(request, "base/delete.html", {'task': task})

# class DeleteView(DeleteView):
#     model = Task
#     context_object_name = 'task'
#     success_url = reverse_lazy('tasks')
