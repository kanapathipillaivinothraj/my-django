from django.shortcuts import render
from django.http import HttpResponse
from App.models import detail_dataBase
# Create your views here.


def Home (request):
    msg = "Hello"
    datas = detail_dataBase.objects.all()
    return render(request,"index.html",{"data":datas,'A' :msg})