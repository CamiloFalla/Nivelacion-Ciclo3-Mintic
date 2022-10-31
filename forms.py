from django import forms


class FormularioCrearServicio(forms.Form):
    
    nombre=forms.CharField()
    especialidad=forms.CharField()
    precio=forms.IntegerField()