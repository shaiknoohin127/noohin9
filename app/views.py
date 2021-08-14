from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def specific1(request):
    return HttpResponse("<h1>specific1 content of string return type</h1>")