from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Home (request):
    A = "<h1>Hello</h1>"
    return HttpResponse(A)