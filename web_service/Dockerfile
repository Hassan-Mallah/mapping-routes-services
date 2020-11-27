FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /web_service

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /web_service/

CMD ["python", "app.py"]
