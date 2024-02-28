FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY prompts.py /app/prompts.py
COPY app.py /app/app.py

COPY .env /app/.env
