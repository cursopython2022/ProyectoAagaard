from socket import fromshare
from django import forms

class ArgentinoFormulario(forms.Form):

    #Especificar los campos
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()

class ExtranjeroFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()

class NacionalizadoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
        