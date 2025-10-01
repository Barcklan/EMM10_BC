# Imagen base
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY breast_cancer_model.pkl breast_cancer_model.pkl

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 5001

# Comando por defecto
CMD ["python", "app.py"]
