# 1. Imagen base ligera
FROM python:3.12-slim

# 2. Variables de entorno para que Python no genere .pyc y muestre logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo en el contenedor
WORKDIR /app

# 4. Instalar dependencias del sistema (necesarias para psycopg2 y herramientas de red)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar el resto del código
COPY . .

# 7. Puerto que usa Render por defecto
EXPOSE 8000

# 8. Comando para arrancar con Gunicorn (más estable que runserver para producción)
# Primero instalaremos gunicorn en el siguiente paso
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core_agro.wsgi:application"]

