FROM python:3.9

ENV workDIRECTORY=/databytes

WORKDIR $workDIRECTORY
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN pip install --upgrade pip

COPY $workDIRECTORY
RUN pip install -r requirements.txt
EXPOSE 8080

CMD python manage.py migrate
CMD python manage.py makemigrations
CMD python manage.py runserver 8080
