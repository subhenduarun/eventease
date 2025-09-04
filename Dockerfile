FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask sqlalchemy

CMD ["python", "backend/app.py"]
