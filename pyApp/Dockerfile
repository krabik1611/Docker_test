FROM python:3.8-alpine3.12
WORKDIR /app
COPY app/ /app/
RUN pip install -r requirements.txt
CMD uvicorn main:app --host 172.18.0.4 --port 4444
