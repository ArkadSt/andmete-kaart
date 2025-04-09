FROM python:3.12.10-alpine3.21
COPY . ./app
WORKDIR /app
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]


