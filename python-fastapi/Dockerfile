FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app

EXPOSE 8000

<<<<<<< HEAD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> 33d59440a3122874a3707a7e08e51eab07d5cd4d
