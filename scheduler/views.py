from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'scheduler/home.html')

def first(request):
    return HttpResponse('<h1>Testing stuff 2</h1>')
