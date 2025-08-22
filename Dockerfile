FROM python:3.10-slim

WORKDIR /app
COPY main.py .

# Installer mysql-connector-python
RUN pip install --no-cache-dir mysql-connector-python

# Lancer le script Python
CMD ["python", "main.py"]
