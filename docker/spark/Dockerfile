FROM apache/spark:3.5.1-scala2.12-java17-python3-ubuntu

LABEL maintainer="alaa"
LABEL project="devops-data-platform"
LABEL component="spark-batch"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/spark

COPY spark/jobs /opt/spark/jobs

USER 185

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD /opt/spark/bin/spark-submit --version || exit 1

CMD ["/opt/spark/bin/spark-submit", "--version"]
