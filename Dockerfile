# Use the official Python 3.9 image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --upgrade pip && pip install pipenv

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

# Collect static files (optional)
# RUN pipenv run python manage.py collectstatic --noinput

# Run database migrations
RUN pipenv run python manage.py migrate

# Create a Django superuser (optional automation)
# You can also comment this out and create one manually
RUN echo "from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" \
    | pipenv run python manage.py shell

# Expose port 8000
EXPOSE 8000

# Start the app
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
