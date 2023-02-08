FROM python:latest
LABEL MAINTAINER='Parsa Khoshvaghti'

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /thecafe

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "thecafe.wsgi:application", "--bind", "0.0.0.0:8000"]
