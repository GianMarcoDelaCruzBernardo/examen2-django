from django.db import migrations
import django.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_proyecto_imagen_imagefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=django.db.models.URLField(
                blank=True,
                null=True,
                verbose_name='Imagen del proyecto',
            ),
        ),
    ]
