#!/usr/bin/env bash
set -e

echo ">>> Instalando dependencias..."
pip install -r requirements.txt

echo ">>> Recopilando archivos estaticos..."
python manage.py collectstatic --no-input

echo ">>> Ejecutando migraciones..."
python manage.py migrate

echo ">>> Limpiando imagenes locales rotas..."
python manage.py limpiar_imagenes

echo ">>> Verificando config Cloudinary..."
python -c "
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion.settings')
django.setup()
import cloudinary
cfg = cloudinary.config()
print('CLOUD_NAME:', cfg.cloud_name if cfg.cloud_name else 'NO CONFIGURADO - FALTA CLOUDINARY_URL')
print('API_KEY:', 'OK' if cfg.api_key else 'NO CONFIGURADO - FALTA CLOUDINARY_URL')
"

echo ">>> Creando superusuario admin..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superusuario admin creado")
else:
    print("Superusuario admin ya existe")
EOF

echo ">>> Build completado exitosamente!"
