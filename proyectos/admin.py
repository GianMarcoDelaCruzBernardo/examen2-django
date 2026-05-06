from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(ModelAdmin):
    list_display  = ('nombre', 'estado', 'fecha_inicio', 'fecha_fin', 'imagen_preview')
    list_filter   = ('estado',)
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('creado_en', 'imagen_preview')

    def imagen_preview(self, obj):
        if obj.imagen:
            try:
                return format_html('<img src="{}" style="height:60px;border-radius:6px;object-fit:cover;" />', obj.imagen.url)
            except Exception:
                return "Error al cargar"
        return "Sin imagen"
    imagen_preview.short_description = "Vista previa"

@admin.register(Tarea)
class TareaAdmin(ModelAdmin):
    list_display  = ('titulo', 'proyecto', 'prioridad', 'estado', 'fecha_limite')
    list_filter   = ('prioridad', 'estado', 'proyecto')
    search_fields = ('titulo', 'descripcion')