# syntax=docker/dockerfile:1
FROM python:3.9
#ENV PYTHONUNBUFFERED 1
#ENV PYTHONDONTWRITEBYTECODE=1
ENV DJANGO_SETTINGS_MODULE=codingTeam.settings
EXPOSE 8000
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["./manage.py", "runserver"]

