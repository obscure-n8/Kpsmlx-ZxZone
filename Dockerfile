ARG STACK_VERSION=24
FROM heroku/heroku:${STACK_VERSION}-build

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 \
    python3-pip \
    python3-venv \
    curl \
    git \
    ffmpeg \
    mediainfo \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/bin/python3.11 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

WORKDIR /app
RUN chmod 777 /app

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R heroku:heroku /app || true

CMD ["bash", "start.sh"]
