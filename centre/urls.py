
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = "home"),
    path('students/', views.alumne, name = "alumne"),
    path('teachers/', views.professor, name = "professor")
]
