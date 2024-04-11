from django.contrib import admin
from django.urls import path
from nomapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.holaMundo, name = "hola"),
    path('about/', views.sobre, name = "about"),
    path('prova/', views.index, name = "prova")
]


