from django.db import migrations
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_proyecto_imagen_cloudinary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=django.db.models.ImageField(
                blank=True,
                null=True,
                upload_to='proyectos/',
                verbose_name='Imagen del proyecto',
            ),
        ),
    ]
