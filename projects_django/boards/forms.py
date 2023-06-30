# importar la librería estándar de Django Forms
from django import forms
from .models import BoardsModel
from django.forms import ModelForm
# Agregando para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Creación de un forms
class InputForm(forms.Form):
    nombres = forms.CharField(max_length = 200)
    apellidos = forms.CharField(max_length = 200)
    prioridad = forms.IntegerField(min_value=1, max_value=3)
    contrasenna = forms.CharField(widget = forms.PasswordInput())


class WidgetForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    prioridad = forms.IntegerField(min_value=1, max_value=3)
    habilitado = forms.BooleanField()
    date = forms.DateField(widget= forms.SelectDateWidget)


#Import BoardMOdel from models.py and Create Form with ModelForm


class BoardsForm(ModelForm):
    class Meta:
        model = BoardsModel
        fields = "__all__"


# Agregado para el registro de usuarios
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user