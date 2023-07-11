from django import forms

class Productosform(forms.Form):
    nombre= forms.CharField()
    categoria= forms.CharField()


class Serviciosform(forms.Form):
    nombre= forms.CharField()
    categoria= forms.CharField()


class Clientesform(forms.Form):
    nombre= forms.CharField()
    dni= forms.IntegerField()
    email= forms.EmailField()
    fechacompra= forms.DateField()
    