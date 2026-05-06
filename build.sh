#!/usr/bin/env bash
set -e

echo ">>> Instalando dependencias..."
pip install -r requirements.txt

echo ">>> Recopilando archivos estáticos..."
python manage.py collectstatic --no-input

echo ">>> Ejecutando migraciones..."
python manage.py migrate

echo ">>> Build completado exitosamente."