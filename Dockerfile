FROM python:3

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /tcc

COPY requirements.txt /tcc

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /tcc

EXPOSE 8000

ENTRYPOINT ["python3"] 

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
