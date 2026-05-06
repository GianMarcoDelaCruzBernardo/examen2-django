from django import forms
from .models import Proyecto, Tarea


class ProyectoForm(forms.ModelForm):
    imagen = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model  = Proyecto
        fields = ['nombre', 'descripcion', 'imagen', 'fecha_inicio', 'fecha_fin', 'estado']
        widgets = {
            'nombre':       forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':  forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin':    forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado':       forms.Select(attrs={'class': 'form-select'}),
        }

    def save(self, commit=True):
        # imagen la maneja la vista directamente, no el form
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class TareaForm(forms.ModelForm):
    class Meta:
        model  = Tarea
        fields = ['proyecto', 'titulo', 'descripcion', 'prioridad', 'estado', 'fecha_limite']
        widgets = {
            'proyecto':     forms.Select(attrs={'class': 'form-select'}),
            'titulo':       forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':  forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'prioridad':    forms.Select(attrs={'class': 'form-select'}),
            'estado':       forms.Select(attrs={'class': 'form-select'}),
            'fecha_limite': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
