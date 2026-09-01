FROM anasty17/mltb:latest

WORKDIR /app

RUN chmod -R 777 /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN sed -i 's/\r$//' *.sh

ENV PORT=8080

CMD ["bash", "start.sh"]
