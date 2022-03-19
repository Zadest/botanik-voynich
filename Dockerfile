FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install pip --upgrade
RUN python -m pip install -r requirements.txt
COPY . /code/
RUN python /code/voynich/manage.py makemigrations
RUN python /code/voynich/manage.py migrate

