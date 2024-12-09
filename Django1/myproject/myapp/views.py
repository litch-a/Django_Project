from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Little Lemon Restraunt!!")

# Create your views here.
