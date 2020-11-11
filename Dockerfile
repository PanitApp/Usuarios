FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev
RUN pip install -r requirements.txt
RUN pip install djangorestframework-simplejwt
COPY . /code/
ARG URL=0.0.0.0:4000

CMD ["sh", "-c", "python manage.py makemigrations usuarios && python manage.py migrate && python manage.py runserver $URL"]
