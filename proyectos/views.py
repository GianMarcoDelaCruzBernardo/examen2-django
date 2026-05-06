from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Proyecto, Tarea
from .forms  import ProyectoForm, TareaForm
import cloudinary.uploader


def subir_imagen_cloudinary(archivo):
    """Sube un archivo a Cloudinary y retorna la URL segura."""
    try:
        resultado = cloudinary.uploader.upload(
            archivo,
            folder='proyectos',
            resource_type='image'
        )
        return resultado.get('secure_url', '')
    except Exception as e:
        print(f"Error Cloudinary: {e}")
        return ''


# ── Proyecto ────────────────────────────────────────────────
def proyecto_lista(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto_lista.html', {'proyectos': proyectos})


def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    tareas   = proyecto.tareas.all()
    return render(request, 'proyecto_detalle.html',
                  {'proyecto': proyecto, 'tareas': tareas})


def proyecto_crear(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            if 'imagen' in request.FILES:
                url = subir_imagen_cloudinary(request.FILES['imagen'])
                if url:
                    proyecto.imagen = url
            proyecto.save()
            messages.success(request, 'Proyecto creado correctamente.')
            return redirect('proyecto_lista')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto_form.html',
                  {'form': form, 'titulo': 'Nuevo Proyecto'})


def proyecto_editar(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES, instance=proyecto)
        if form.is_valid():
            proyecto = form.save(commit=False)
            if 'imagen' in request.FILES:
                url = subir_imagen_cloudinary(request.FILES['imagen'])
                if url:
                    proyecto.imagen = url
            proyecto.save()
            messages.success(request, 'Proyecto actualizado.')
            return redirect('proyecto_lista')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyecto_form.html',
                  {'form': form, 'titulo': 'Editar Proyecto'})


def proyecto_eliminar(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado.')
        return redirect('proyecto_lista')
    return render(request, 'proyecto_confirmar_eliminar.html',
                  {'objeto': proyecto, 'tipo': 'Proyecto'})


# ── Tarea ───────────────────────────────────────────────────
def tarea_lista(request):
    tareas = Tarea.objects.select_related('proyecto').all()
    return render(request, 'tarea_lista.html', {'tareas': tareas})


def tarea_detalle(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tarea_detalle.html', {'tarea': tarea})


def tarea_crear(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea creada correctamente.')
            return redirect('tarea_lista')
    else:
        form = TareaForm()
    return render(request, 'tarea_form.html',
                  {'form': form, 'titulo': 'Nueva Tarea'})


def tarea_editar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada.')
            return redirect('tarea_lista')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tarea_form.html',
                  {'form': form, 'titulo': 'Editar Tarea'})


def tarea_eliminar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, 'Tarea eliminada.')
        return redirect('tarea_lista')
    return render(request, 'proyecto_confirmar_eliminar.html',
                  {'objeto': tarea, 'tipo': 'Tarea'})
