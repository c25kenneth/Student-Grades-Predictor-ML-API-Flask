FROM python:3.8

WORKDIR /gradepredictor

COPY requirements.txt .
COPY model.py .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/app.py"]