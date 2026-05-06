from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import Proyecto, Tarea


@admin.register(Proyecto)
class ProyectoAdmin(ModelAdmin):
    list_display  = ['nombre', 'estado', 'fecha_inicio', 'fecha_fin', 'vista_imagen', 'creado_en']
    list_filter   = ['estado']
    search_fields = ['nombre', 'descripcion']
    ordering      = ['-creado_en']
    readonly_fields = ['vista_imagen_grande']

    fieldsets = (
        ('Informacion General', {
            'fields': ('nombre', 'descripcion', 'estado')
        }),
        ('Imagen', {
            'fields': ('imagen', 'vista_imagen_grande')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin')
        }),
    )

    def vista_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:6px;" />', obj.imagen.url)
        return '-'
    vista_imagen.short_description = 'Imagen'

    def vista_imagen_grande(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="200" style="border-radius:10px;" />', obj.imagen.url)
        return 'Sin imagen'
    vista_imagen_grande.short_description = 'Vista previa'


@admin.register(Tarea)
class TareaAdmin(ModelAdmin):
    list_display  = ['titulo', 'proyecto', 'prioridad', 'estado', 'fecha_limite']
    list_filter   = ['prioridad', 'estado', 'proyecto']
    search_fields = ['titulo', 'descripcion']
    ordering      = ['prioridad', '-creado_en']

    fieldsets = (
        ('Informacion de la Tarea', {
            'fields': ('proyecto', 'titulo', 'descripcion')
        }),
        ('Estado y Prioridad', {
            'fields': ('prioridad', 'estado', 'fecha_limite')
        }),
    )
