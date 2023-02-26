from django.shortcuts import render
from django.http import HttpResponse
from App.models import detail_dataBase
from App.forms import detail_dataBase_Froms
# Create your views here.


def Home (request):
    form = detail_dataBase_Froms()
    datas = detail_dataBase.objects.all()
    return render(request,"index.html",{"data":datas,'A' :form})