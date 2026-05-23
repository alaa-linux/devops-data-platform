FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir requests prometheus_client \
    && useradd -m appuser \
    && chown -R appuser:appuser /app

COPY spark_exporter.py /app/spark_exporter.py

USER appuser

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:9400/metrics', timeout=5)" || exit 1

CMD ["python", "/app/spark_exporter.py"]
