# Verifica el contenido actual
cat build.sh

# Vamos a reescribir el archivo con saltos de línea correctos
$content = @'
#!/usr/bin/env bash
set -e

echo ">>> Instalando dependencias..."
pip install -r requirements.txt

echo ">>> Recopilando archivos estáticos..."
python manage.py collectstatic --no-input

echo ">>> Ejecutando migraciones..."
python manage.py migrate

echo ">>> Build completado exitosamente."
'@

# Guardar el archivo (PowerShell usa UTF-8 sin BOM)
[System.IO.File]::WriteAllText("build.sh", $content)

# Verificar que se guardó bien
cat build.sh