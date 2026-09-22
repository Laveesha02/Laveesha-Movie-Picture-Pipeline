FROM python:3.10-slim

WORKDIR /app

COPY Pipfile .

RUN pip install pipenv && \
    pipenv install --system --deploy

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
