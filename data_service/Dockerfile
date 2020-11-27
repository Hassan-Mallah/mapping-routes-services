FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /data_service

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /data_service/

CMD ["python", "app.py"]
