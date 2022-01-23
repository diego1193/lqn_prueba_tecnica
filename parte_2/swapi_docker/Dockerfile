FROM python:3.8.5

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
copy . /code/

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "swapi_docker.wsgi:application"]