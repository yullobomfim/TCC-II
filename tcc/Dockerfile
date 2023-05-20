FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip

WORKDIR /tcc
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
