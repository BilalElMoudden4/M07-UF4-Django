from django.db import models

class Usuari(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    assignatures = models.CharField(max_length=200)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

class Rol(models.Model):
    nom = models.CharField(max_length=50)

class db(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
