from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request): 
    return render(request, 'home.html')

def proj4(request): 
    return render(request, 'proj4.html')
 
def proj3(request):
    return render(request, 'proj3.html')

def cartoonify(request):
    return render(request, 'cartoonify.html')

def nlptext(request): 
    return render(request, 'nlptext.html')

def nfl_ml(request):
    return render(request, 'nfl_ml.html')

def preprocessing(request): 
    return render(request, 'preprocessing.html')

def annotation(request): 
    return render(request, 'annotation.html')

def analysis(request): 
    return render(request, 'analysis.html')

def train(request):
    return render(request, 'train.html')

def anytime(request):
    return render(request, 'anytime.html')

def resume(request):
    return render(request, 'resume.html')

