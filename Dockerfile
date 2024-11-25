FROM python:3.10-slim


COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


RUN mkdir /app
WORKDIR /app
COPY . .


# Locale
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8


CMD ["python", "main.py"]
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
