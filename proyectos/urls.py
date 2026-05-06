from django.urls import path
from . import views

urlpatterns = [
    # Proyectos
    path('',                       views.proyecto_lista,    name='proyecto_lista'),
    path('proyecto/<int:pk>/',     views.proyecto_detalle,  name='proyecto_detalle'),
    path('proyecto/nuevo/',        views.proyecto_crear,    name='proyecto_crear'),
    path('proyecto/<int:pk>/editar/',   views.proyecto_editar,   name='proyecto_editar'),
    path('proyecto/<int:pk>/eliminar/', views.proyecto_eliminar, name='proyecto_eliminar'),

    # Tareas
    path('tareas/',                views.tarea_lista,    name='tarea_lista'),
    path('tarea/<int:pk>/',        views.tarea_detalle,  name='tarea_detalle'),
    path('tarea/nueva/',           views.tarea_crear,    name='tarea_crear'),
    path('tarea/<int:pk>/editar/',   views.tarea_editar,   name='tarea_editar'),
    path('tarea/<int:pk>/eliminar/', views.tarea_eliminar, name='tarea_eliminar'),
]
