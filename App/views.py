from django.shortcuts import render,redirect
from django.http import HttpResponse
from App.models import detail_dataBase
from App.forms import detail_dataBase_Froms
from App.model_form import Model_forms
# Create your views here.


def Home (request):
    form = detail_dataBase_Froms()
    datas = detail_dataBase.objects.all()
    model_form = Model_forms()
    if request.method ==  "POST":
        Database = Model_forms(request.POST)
        if Database.is_valid():
            Database.save()
            redirect('index')
    return render(request,"index.html",{"data":datas,'A' :form, 'model_form':model_form})

def Update (request):
    form = detail_dataBase_Froms()
    datas = detail_dataBase.objects.all()
    model_form = Model_forms()
    if request.method ==  "POST":
        Database = Model_forms(request.POST)
        if Database.is_valid():
            Database.save()
            redirect('index')
    return render(request,"index.html",{"data":datas,'A' :form, 'model_form':model_form})