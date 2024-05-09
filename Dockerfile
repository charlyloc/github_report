FROM python:3.10-slim

WORKDIR /app

ENV OWNER freeCodeCamp
ENV REPO freeCodeCamp

COPY app/ /app

RUN pip install -r requirements.txt

CMD ["python", "github_report.py"]