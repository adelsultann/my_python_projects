from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from .models import Movie


# Create your views here.
def show_image(request):
    moives = Movie.objects.all()
    img = open('../static/media/')




def home(request):
    moives = Movie.objects.all()
    context = {'movies': moives}
    return render(request, 'base/home.html', context)
