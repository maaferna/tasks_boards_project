from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('formsave', FormModelSaveView.as_view(), name='saveform'),
    path('fecha/<name>', obtenerFecha, name='index'),
    path('menu/', menuView, name='menu'),
    path('mostrar/', mostrar, name='mostrar'),
    path('datosform/', datosform_view, name='datosform'),
    path('widget_home/', widget_view, name='widget'),
    path('boardsform/', boardsform_view, name='boardsform'),
    path('registro/', registro_view, name="registro"), 
    path('login/', login_view,name='login'),
    path('logout/', logout_view, name='logout'),
    path('boards_list', boards_list, name='listed'),
    ]