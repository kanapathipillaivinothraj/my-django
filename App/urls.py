from django.urls import path
from App import views
# 

urlpatterns = [
    path('', views.Home,name="index"),
    path('', views.Update, name="Update"),
]