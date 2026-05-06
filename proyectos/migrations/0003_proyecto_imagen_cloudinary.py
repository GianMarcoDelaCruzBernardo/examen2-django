from django.db import migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_proyecto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=cloudinary.models.CloudinaryField(
                blank=True,
                null=True,
                verbose_name='Imagen del proyecto',
                max_length=255,
            ),
        ),
    ]
