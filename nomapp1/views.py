from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def holaMundo(requests):
    return HttpResponse("Hello World")

def sobre(requests):
    return HttpResponse("<h1>About")

def index(requests):
    professor = {"name":"Bilal", "surname":"El Moudden", "age":"17"}
    template = loader.get_template('index.html')
    dades = template.render({'nombre':professor["name"], 'apellido':professor["surname"], 'edad':professor["age"]})
    return HttpResponse(dades)

