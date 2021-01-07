FROM python:3.8-slim


COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0" ]