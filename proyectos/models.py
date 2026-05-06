from django.db import models
class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('activo',     'Activo'),
        ('pausado',    'Pausado'),
        ('completado', 'Completado'),
        ('cancelado',  'Cancelado'),
    ]

    nombre       = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion  = models.TextField(blank=True, verbose_name='Descripcion')
    imagen       = models.ImageField(upload_to='proyectos/', blank=True, null=True,
                                     verbose_name='Imagen del proyecto')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_fin    = models.DateField(null=True, blank=True, verbose_name='Fecha de fin')
    estado       = models.CharField(max_length=20, choices=ESTADO_CHOICES,
                                    default='activo', verbose_name='Estado')
    creado_en    = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering            = ['-creado_en']

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    PRIORIDAD_CHOICES = [
        ('baja',    'Baja'),
        ('media',   'Media'),
        ('alta',    'Alta'),
        ('urgente', 'Urgente'),
    ]
    ESTADO_CHOICES = [
        ('pendiente',   'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada',  'Completada'),
        ('cancelada',   'Cancelada'),
    ]

    proyecto     = models.ForeignKey(Proyecto, on_delete=models.CASCADE,
                                     related_name='tareas', verbose_name='Proyecto')
    titulo       = models.CharField(max_length=200, verbose_name='Titulo')
    descripcion  = models.TextField(blank=True, verbose_name='Descripcion')
    prioridad    = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES,
                                    default='media', verbose_name='Prioridad')
    estado       = models.CharField(max_length=15, choices=ESTADO_CHOICES,
                                    default='pendiente', verbose_name='Estado')
    fecha_limite = models.DateField(null=True, blank=True, verbose_name='Fecha limite')
    creado_en    = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering            = ['prioridad', '-creado_en']

    def __str__(self):
        return f'{self.titulo} ({self.proyecto})'
