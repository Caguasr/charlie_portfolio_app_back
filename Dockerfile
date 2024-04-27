FROM python:latest

WORKDIR /code/src
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade  -r requirements.txt

COPY /app /code/src/app
ENV DB_HOST=focused_wu
ENV DB_PORT=5432
ENV DB_USERNAME=postgres
ENV DB_PASSWORD=12345
ENV DB_NAME=portfolio
ENV SECRET_KEY=12345
ENV TIME_EXPIRES_TOKEN=30
EXPOSE 8000
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]

