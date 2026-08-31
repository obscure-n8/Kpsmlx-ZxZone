FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git ffmpeg mediainfo \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN pip3 install --no-cache-dir --upgrade setuptools pip uv
RUN uv pip install --system --no-cache pymediainfo pyaes

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]
