from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre= models.CharField(max_length=30)
    categoria= models.CharField(max_length=30)


class Servicios(models.Model):
    nombre= models.CharField(max_length=30)
    categoria= models.CharField(max_length=30)


class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    dni= models.IntegerField()
    email= models.EmailField()
    fechacompra= models.DateField()




