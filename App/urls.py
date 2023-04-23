from django.urls import path
from App import views
from django.contrib import admin
# 

urlpatterns = [
    path('mystore/', admin.site.urls),
    path('', views.Home,name="index"),
    # path('', views.Update, name="Update"),
]