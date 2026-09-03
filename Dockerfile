FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg \
    unzip \
    p7zip-full \
    mediainfo \
    aria2 \
    qbittorrent-nox \
    build-essential \
    gcc \
    python3-dev \
    libssl-dev \
    libmagic1 \
    locales \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]
