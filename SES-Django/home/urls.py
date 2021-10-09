from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [    
    path('', views.index,name="index"),
    path('home', views.home,name="home"),
    path('registerevent/<eid>/', views.registerEvent,name="registerEvent"),
    path('successfulsubmition', views.successfulSubmit,name="successfulSubmit"),
    path('downloadjson', views.downloadJson,name="downloadJson"),
    ]