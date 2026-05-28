FROM apache/superset:4.1.1

USER root

RUN uv pip install --python /app/.venv/bin/python psycopg2-binary

USER superset

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:8088/health || exit 1
