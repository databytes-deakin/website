FROM python:3.9

ENV DIRECTORY=/databytes
ENV PORT=8000

WORKDIR ${DIRECTORY}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN pip install --upgrade pip

COPY . .
RUN pip install -r requirements.txt


EXPOSE ${PORT}

COPY ${DIRECTORY} ./
RUN python manage.py migrate
RUN python manage.py makemigrations
CMD ["python manage.py runserver 8080"]
