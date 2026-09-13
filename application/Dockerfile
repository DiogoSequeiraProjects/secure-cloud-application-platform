FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip setuptools \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip install --no-cache-dir "msgpack>=1.2.1" \
    && rm -f /usr/local/lib/python3.13/site-packages/pip/_vendor/bom.cdx.json

COPY . .

ENV FLASK_HOST=0.0.0.0

EXPOSE 5000

CMD ["python", "app.py"]