from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Home (request):
    msg = "Hello"
    return render(request,"index.html",{"A":msg})