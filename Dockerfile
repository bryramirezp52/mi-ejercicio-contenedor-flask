FROM python:3.10-slim
WORKDIR /app

# instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copiar la aplicación
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
