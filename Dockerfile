FROM python:3.8

WORKDIR /app

# Ustawienia proxy dla HTTP i HTTPS
ARG http_proxy
ARG https_proxy
ENV http_proxy=$http_proxy
ENV https_proxy=$https_proxy

COPY requirements.txt .
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000" ]
