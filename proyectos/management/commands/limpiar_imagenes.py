from django.core.management.base import BaseCommand
from proyectos.models import Proyecto


class Command(BaseCommand):
    help = 'Limpia referencias de imágenes locales rotas (no-Cloudinary) de la base de datos'

    def handle(self, *args, **options):
        proyectos = Proyecto.objects.exclude(imagen='').exclude(imagen__isnull=True)
        limpiados = 0

        for p in proyectos:
            valor = str(p.imagen)
            # Las URLs de Cloudinary empiezan con "http" o tienen "/" (public_id con carpeta)
            # Las rutas locales rotas son como "proyectos/foto.jpg" sin ser una URL de Cloudinary
            # Si el campo no contiene una URL de cloudinary válida, lo limpiamos
            es_cloudinary = (
                valor.startswith('http') or
                valor.startswith('image/upload') or
                'cloudinary' in valor
            )
            if not es_cloudinary:
                self.stdout.write(f'  Limpiando imagen rota: {valor} (proyecto: {p.nombre})')
                p.imagen = None
                p.save(update_fields=['imagen'])
                limpiados += 1

        if limpiados:
            self.stdout.write(self.style.SUCCESS(
                f'✅ {limpiados} imágenes locales rotas eliminadas de la BD. '
                f'Sube las imágenes nuevamente desde el formulario.'
            ))
        else:
            self.stdout.write(self.style.SUCCESS('✅ No hay imágenes rotas que limpiar.'))
