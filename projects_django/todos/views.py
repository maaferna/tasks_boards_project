from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Task
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt

def index(request):
  tasks = Task.objects.all()
  context = {'tasks': tasks}
  return render(request, "todos/index.html", context)


def todos_view(request):
  if request.method == "POST":
      task = Task()
      task.title = request.POST.get("title")
      task.save()
      return JsonResponse({"id": task.id, "title": task.title, "completed":task.completed})
  else:
      t = Task.objects.all()
      tobjects = []
      for x in t:
        tobjects.append({
        	'id': x.id,
        	'title': x.title,
        	'completed': x.completed})
      return JsonResponse(tobjects, safe= False)


def task_status(request, id):
    task = Task.objects.get(id = id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({"id": task.id, "title": task.title, "completed":task.completed})

def task_edit(request, id):
    task = Task.objects.get(id = id)
    task.title = request.POST.get("title")
    task.save()
    return JsonResponse({"id": task.id, "title": task.title, "completed":task.completed})

def task_delete(request, id):
    if request.method == "POST":
        task = Task.objects.get(id = id)
        try:
            task.delete()
        except:
            print("Error to delete ID")
    t = Task.objects.all()
    tobjects = []
    for x in t:
        tobjects.append({
        	'id': x.id,
        	'title': x.title,
        	'completed': x.completed})
    context = {"tasks":tobjects}
    return render(request, "todos/index.html", context)
