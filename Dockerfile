FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"

CMD ["python", "main.py"]
