from django import forms


class ObraFormulario(forms.Form):
    tipo = forms.CharField(max_length=40)
    inicio = forms.CharField()
    
    
class ObreroFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()


class ArquitectoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    matricula = forms.CharField(max_length=30)

class BusquedaObraFormulario(forms.Form):
    tipo = forms.CharField(max_length=30)