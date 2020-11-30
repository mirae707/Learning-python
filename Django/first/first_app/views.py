from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My third project</em>")

def pic(request):
    pic_dict = {'pic_insert': 'Skelleton'}
    return render(request, 'first_app/pic.html', context=pic_dict)
