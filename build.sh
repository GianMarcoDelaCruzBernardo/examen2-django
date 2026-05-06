#!/usr/bin/env bash
set -e

echo ">>> Instalando dependencias..."
pip install -r requirements.txt

echo ">>> Recopilando archivos estáticos..."
python manage.py collectstatic --no-input

echo ">>> Ejecutando migraciones..."
python manage.py migrate

echo ">>> Build completado exitosamente."


# ============================================
# SUPERUSUARIO PERMANENTE
# Se ejecuta en cada deploy sin perder datos
# ============================================
echo ">>> Verificando superusuario admin..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model;
User = get_user_model();

# Crear o actualizar superusuario admin
user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'is_superuser': True,
        'is_staff': True
    }
)

# Siempre actualizar la contraseña a 'admin'
user.set_password('admin')
user.is_superuser = True
user.is_staff = True
user.save()

if created:
    print("✅ Superusuario admin CREADO exitosamente")
else:
    print("✅ Superusuario admin VERIFICADO y contraseña actualizada")
EOF
