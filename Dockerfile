FROM python:3.11-slim

# Install build deps and cleanup to keep image small
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Ensure Python can import the application modules from /app when running tests inside the container
ENV PYTHONPATH=/app

# Copy requirements first for layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# WYMUSZAMY PORT 80 DLA AZURE
EXPOSE 80

# Używamy portu 80 w serwerze gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]