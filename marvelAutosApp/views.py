from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_Page(requests):
    return HttpResponse("My MarvelAutos Project..!")