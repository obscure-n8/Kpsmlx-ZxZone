# ZxZone-Master-MLTB - Heroku Dockerfile
FROM heroku/python:3.11

WORKDIR /app

# Install system dependencies (no apt-get update needed)
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg \
    mediainfo \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Set permissions
RUN chmod 777 /app

CMD ["bash", "start.sh"]
