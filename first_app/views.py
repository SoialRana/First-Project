from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is my first django page")

def about(request):
    return HttpResponse("this is about page")