# My-django

CURD &amp; Authentication

# Django version - 4.1.4

# requirements

asgiref 3.5.2  
autopep8 2.0.0  
certifi 2022.9.24
charset-normalizer 2.1.1  
Django 4.1.4  
django-cors-headers 3.13.0  
django-pyodbc-azure 2.1.0.0  
djangorestframework 3.14.0  
djongo 1.3.6  
dnspython 2.2.1  
docutils 0.19  
et-xmlfile 1.1.0  
Kivy 2.1.0
kivy-deps.angle 0.3.3
kivy-deps.glew 0.3.1
kivy-deps.gstreamer 0.3.3
kivy-deps.sdl2 0.4.5
Kivy-Garden 0.1.5
kivymd 1.1.1
npm 0.1.1
openpyxl 3.0.10
optional-django 0.1.0
Pillow 9.2.0
pip 22.2.2
pycodestyle 2.10.0
Pygments 2.13.0
pymongo 4.3.2
pyodbc 4.0.35
pypiwin32 223
pytube 12.1.0
pytz 2022.6
pywin32 305
requests 2.28.1
setuptools 63.2.0
sqlparse 0.2.4
tomli 2.0.1
tzdata 2022.5
urllib3 1.26.13

# Start the project #1

django-admin startproject Project .
py manage.py runserver

# Start the App #2

py manage.py startapp App

# Register the app #3

INSTALLED_APPS = [
'App',
]

# Create App.urls in Project.urls file #4

from django.urls import path,include // import include
urlpatterns = [
path('', include('App.urls')),
]

# Create New App.urls file #5

from django.urls import path
from App import views // import views
urlpatterns = [
path('', views.Home,name="index"),
]

# Create a Function #6

from django.shortcuts import render
from django.http import HttpResponse // import HttpResponse

def Home (request):
A = "<h1>Hello</h1>"
return HttpResponse(A)

# Create Template and connect to settings.py file #7

1. Create template folder and create a new html file (index.html)
2. settings.py =>
   import os
   TEMPLATES = [
   {
   'DIRS': [os.path.join(BASE_DIR/"Template")], // connect the template folder
   }
   ]
3. call the function
   def Home (request):
   return render(request,"index.html")

# Create static and connect to settings.py file #8

1. Create Static folder and create a new css file (style.css)
2. settings.py =>
   STATICFILES_DIRS = [BASE_DIR/"Static"] // Create to STATICFILES_DIRS = [BASE_DIR/"Static"] for connect the Static folder
3. index.html =>
{% load static %} <!-- inbuild function for load static -->
<link rel="stylesheet" href="{% static 'style.css' %}"> // static => inbuild static variable & 'style.css' => file path eg:- style/style.css
<img src="{% static 'img/home.png' %}" alt="image" srcset="" width="100"> // static => inbuild static variable & 'img/home.png' => file path
<script src="{% static 'jsfile/index.js' %}"></script> // static => inbuild static variable & 'jsfile/index.js' => file path

# MVT => Model View Template & Admin User Account #9

1. App => models.py
Create a model class 
    class detail_dataBase(models.Model):
        No = models.IntegerField()
        Name = models.CharField(max_length=255,null=False,blank=False)
        Address = models.TextField(max_length=255,null=False,blank=False)
        Image = models.ImageField()
        Links = models.URLField(null=True,blank=True)
        Salary = models.FloatField()

        def __str__(self): // database name
            return self.Name // show name tag

2. makemigrations and migrate => 
    Terminal or CMD 
        makemigrations // py manage.py makemigrations App
        migrate // py manage.py migrate
        check database sqlmigrate Appname databasenumber // py manage.py sqlmigrate Appname databasenumber :- py manage.py sqlmigrate App 0002

3. admin User => 
    Terminal or CMD 
        py manage.py createsuperuser


4. App => admin.py
    Register the model 
        from Appname.models import  Classname // from App.models import detail_dataBase

        class controaler_data(admin.ModelAdmin):
            details = ['No','Name','Address','Image','Links','Salary']

        admin.site.register(detail_dataBase,controaler_data) // detail_dataBase -> register the database , controaler_data -> controle the database

5. View the Data
    App => Views.py 

    from App.models import detail_dataBase // import the detail_dataBase
    def Home (request):
        msg = "Hello"
        datas = detail_dataBase.objects.all()
        return render(request,"index.html",{"data":datas,'A' :msg})

    idex.html =>
    {% if data %}
        {% for 1_data in data %}
            <h3>{{1_data.No}}</h3>
            <h3>{{1_data.Name}}</h3>
            <h3>{{1_data.Address}}</h3>
            <h3>{{1_data.Image}}</h3>
            <h3>{{1_data.Links}}</h3>
            <h3>{{1_data.Salary}}</h3>
        {% endfor %}
    {% else %}
        <h3> nodata</h3>
    {% endif %}

    
