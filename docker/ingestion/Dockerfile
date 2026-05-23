FROM python:3.12-slim

LABEL maintainer="alaa"
LABEL project="devops-data-platform"
LABEL component="ingestion"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY scripts/ingestion/fetch_api_sales.py /app/fetch_api_sales.py

RUN useradd -m appuser

USER appuser

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD python --version || exit 1

CMD ["python", "/app/fetch_api_sales.py"]
