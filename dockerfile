FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUMBUFFERED 1
RUN apt-get update 
WORKDIR /todo
COPY . /todo/
RUN pip install --upgrade pip && pip install -r requirements.txt 
VOLUME [ "/todo" ]
EXPOSE 8000
# CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8080
#CMD ["%%CMD%%"] 