from tokenize import PseudoExtras
from django.views.generic import TemplateView
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from .forms import InputForm, WidgetForm, BoardsForm, RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import BoardsModel

class Persona(object):
  def __init__ (self, nombre, apellido):
    self.nombre=nombre
    self.apellido=apellido 

def datosform_view(request):
 # la logica de la vista se implementa aqui
    print(request.GET)
    context = {}
    context['form'] = InputForm()
    return render(request, "datosform.html", context)

def widget_view(request):
    context = {}
    form = WidgetForm(request.POST or None)
    context['form'] = form
    return render(request, "widget_home.html", context)

class IndexPageView(TemplateView):
  template_name = "index.html"

class FormModelSaveView(TemplateView):
  template_name = "form_model_save.html"

def obtenerFecha(request, name):
  fechaActual = datetime.datetime.now()
  context = { 'fecha' : fechaActual, 'name' : name}
  return render(request, 'fecha.html', context)

def menuView(request):
  template_name = 'menu.html'
  return render(request, template_name)

def mostrar(request):
  persona = Persona("Marco", "Parra")
  context = {'nombre' : persona.nombre, "apellido" : persona.apellido}
  return render(request, "templatesexample.html", context)


def boardsform_view(request):
   context = {}
   form = BoardsForm(request.POST or None, request.FILES or None)
   if form.is_valid():
      form.save()
      return HttpResponseRedirect('/boards/save')
   context['form'] = form
   return render(request, "datosform.html", context)


def registro_view(request):
  if request.method == "POST":
    form = RegistroUsuarioForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, "Registrado Satisfactoriamente." )
      return HttpResponseRedirect('/menu')
    messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
  form = RegistroUsuarioForm()
  return render (request=request, template_name="registration/registro.html", context={"register_form":form})



def login_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,
      password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"Iniciaste sesión como: {username}.")
        return HttpResponseRedirect('menu/')
      else:
        messages.error(request,"Invalido username o password.")
    else:
      messages.error(request,"Invalido username o password.")
  form = AuthenticationForm()
  return render(request=request, template_name="registration/login.html",context={"login_form":form})



def logout_view(request):
  logout(request)
  messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
  return HttpResponseRedirect('menu/') 


def boards_list(request):
  boards = BoardsModel.objects.all()
  context = {'board_list': boards}
  return render(request, 'boards_list.html', context=context)