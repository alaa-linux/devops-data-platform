FROM python:3.12-slim

LABEL maintainer="alaa"
LABEL project="devops-data-platform"
LABEL component="machine-learning"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY docker/ml/requirements.txt /requirements.txt

RUN pip install --default-timeout=300 --no-cache-dir -r /requirements.txt \
    && useradd -m appuser \
    && mkdir -p /app/models /app/scripts /app/outputs \
    && chown -R appuser:appuser /app

USER appuser

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD python --version || exit 1

CMD ["python", "--version"]
