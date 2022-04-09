FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=codingTeam.settings
EXPOSE 8000
WORKDIR /my_app/default/docs
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
CMD ["./manage.py", "runserver"]
