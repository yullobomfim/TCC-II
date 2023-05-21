FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y

WORKDIR /tcc
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
