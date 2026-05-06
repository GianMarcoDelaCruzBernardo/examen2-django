#!/usr/bin/env bash
set -e

echo ">>> Instalando dependencias..."
pip install -r requirements.txt

echo ">>> Recopilando archivos estáticos..."
python manage.py collectstatic --no-input

echo ">>> Ejecutando migraciones..."
python manage.py migrate

echo ">>> Limpiando imágenes locales rotas..."
python manage.py limpiar_imagenes

echo ">>> Creando superusuario admin..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("✅ Superusuario admin creado")
else:
    print("✅ Superusuario admin ya existe")
EOF

echo ">>> Build completado exitosamente!"