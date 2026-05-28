#!/usr/bin/env bash
set -e

echo "[INFO] Running SQL reports..."

docker exec -i postgres-warehouse psql -U warehouse_user -d warehouse -f /dev/stdin < analytics/sql_reports/incidents_report.sql
docker exec -i postgres-warehouse psql -U warehouse_user -d warehouse -f /dev/stdin < analytics/sql_reports/performance_report.sql
docker exec -i postgres-warehouse psql -U warehouse_user -d warehouse -f /dev/stdin < analytics/sql_reports/airflow_report.sql
docker exec -i postgres-warehouse psql -U warehouse_user -d warehouse -f /dev/stdin < analytics/sql_reports/kafka_report.sql
docker exec -i postgres-warehouse psql -U warehouse_user -d warehouse -f /dev/stdin < analytics/sql_reports/spark_report.sql

echo "[INFO] SQL reports completed."
