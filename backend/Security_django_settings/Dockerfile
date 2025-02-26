# Використовуємо Python
FROM python:3.11

WORKDIR /app

# Встановлюємо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код
COPY . .

# Перевіряємо, чи є міграції
RUN python manage.py migrate

EXPOSE 8000

# Запускаємо сервер Gunicorn
CMD ["gunicorn", "Security_django_settings.wsgi:application", "--bind", "0.0.0.0:8000"]
