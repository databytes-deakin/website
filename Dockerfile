FROM python:3.9

ENV DIRECTORY=/databytes

WORKDIR ${DIRECTORY}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN pip install --upgrade pip
RUN pip install django

COPY . .


EXPOSE 800

COPY ${DIRECTORY} ./
CMD ["python manage.py migrate", "python manage.py makemigrations", "python manage.py runserver 800"]
