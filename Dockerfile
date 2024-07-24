# Usa una imagen base con Python
FROM python:3.12-slim

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos (dependencias) al contenedor
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación al contenedor
COPY . /app/

# Expone el puerto en el que FastAPI servirá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]