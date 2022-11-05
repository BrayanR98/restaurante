from socket import fromshare
from turtle import textinput
from django import forms

class FormularioEmpleados (forms.Form):
    CARGO=(
        (1,'Cheff'),
        (2,'Administrador'),
        (3,'Mesero'),
        (4,'Ayudante')
    )
    nombre = forms.CharField(
        required=True,
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
        
    )
    apellidos = forms.CharField(
        required=True,
        max_length=10,
        widget= forms.TextInput(attrs={'class' : 'form-control mb-3'})
    )
    foto = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class' : 'form-control mb-3'})
        
    )
    
    tipo = forms.ChoiceField(
        required=True,
        widget= forms.Select(attrs={'class' : 'form-select mb-3'}),
        choices=CARGO
    )
    