#!/usr/bin/env bash
set -e

echo "[INFO] Running all CSV exports..."

python analytics/exports/export_sales_csv.py
python analytics/exports/export_kpi_csv.py
python analytics/exports/export_dashboard_summary.py

echo "[INFO] All CSV exports completed."
