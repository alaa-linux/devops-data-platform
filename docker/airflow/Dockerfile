FROM apache/airflow:2.9.3

LABEL maintainer="alaa"
LABEL project="devops-data-platform"
LABEL component="airflow-orchestration"

COPY docker/airflow/requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

USER airflow

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD python -c "import airflow; print(airflow.__version__)" || exit 1
