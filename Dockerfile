FROM python:3.9

ENV DIRECTORY=/databytes
ENV PORT=8000

WORKDIR ${DIRECTORY}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN pip install --upgrade pip

COPY ${DIRECTORY} ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE ${PORT}

CMD ["python manage.py runserver 8080"]
