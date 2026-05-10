FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install flask flask-cors psycopg2-binary

CMD ["python", "app.py"]