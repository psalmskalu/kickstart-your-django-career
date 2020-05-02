from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world!<h2>")

def add(request):
    return HttpResponse("<h1>Add a new product</h2><br><hr>")

