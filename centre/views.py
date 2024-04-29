from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home (request):
    return HttpResponse("Hello")

def alumne(request):
    alumnes = [
        {"nom": "Bilal", "cognom1": "El Moudden", "cognom2": "El Maslouhi", "correu": "bilal@itibcn.cat", "curs": "DAW 2B", "Moduls_Matriculats": "6", "rol": "alumne"},
        {"nom": "Marco", "cognom1": "Soliz", "cognom2": "Antonio", "correu": "marco@itibcn.cat", "curs": "DAW 2B", "Moduls_Matriculats": "3", "rol": "alumne"},
        {"nom": "Marc", "cognom1": "Cuzcano", "cognom2": "Cuzcano2", "correu": "marc@itibcn.cat", "curs": "DAW 2B", "Moduls_Matriculats": "4", "rol": "alumne"},
        {"nom": "Jostin", "cognom1": "Cabascango", "cognom2": "Cabascango", "correu": "jostin@itibcn.cat", "curs": "DAW 2B", "Moduls_Matriculats": "7", "rol": "alumne"},
        {"nom": "Aitor", "cognom1": "El Moudden", "cognom2": "El Maslouhi", "correu": "bilal@itibcn.cat", "curs": "DAW 2B", "Moduls_Matriculats": "9", "rol": "alumne"}
    ]
    context = {
        "alumnos": alumnes
    }
    return render(request, 'indexAlumnes.html', context)


def professor(request):
    professors = [
        {"nom": "Oriol", "cognom1": "roca", "cognom2": "roca2", "correu": "oriol@itibcn.cat", "curs": "DAW 2B", "rol": "professor"},
        {"nom": "Roger", "cognom1": "sobrino", "cognom2": "sobrino2", "correu": "roger@itibcn.cat", "curs": "DAW 2B", "rol": "professor"},
        {"nom": "Juanma", "cognom1": "sanchez", "cognom2": "sanchez2", "correu": "juanma@itibcn.cat", "curs": "DAW 2B", "rol": "professor"},
        {"nom": "Carlota", "cognom1": "bernat", "cognom2": "bernat2", "correu": "carlota@itibcn.cat", "curs": "DAW 2B", "rol": "professor"},
        {"nom": "Jordi", "cognom1": "quesada", "cognom2": "quesada2", "correu": "jordi@itibcn.cat", "curs": "DAW 2B", "rol": "professor"}
    ]
    context = {
        "profesores": professors
    }
    return render(request, 'indexProfessors.html', context)
