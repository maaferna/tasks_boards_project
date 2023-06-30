from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home_todos'),
    path('tasks.json', todos_view, name="import_json"),
    path('task/<id>/toggle.json', task_status, name="import_json_edit_status"),
    path('task/<id>/edit.json', task_edit, name="edit_task"),
    path('task/<id>/delete.json', task_delete, name="delete_task"),
    ]
