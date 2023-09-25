from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request): 
    return render(request, 'home.html')

def proj4(request): 
    return render(request, 'proj4.html')
 
def proj3(request):
    return render(request, 'proj3.html')