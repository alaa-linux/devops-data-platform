#!/usr/bin/env bash
set -e

echo "[INFO] Generating charts..."

python analytics/pdf_reports/generate_revenue_chart.py

echo "[INFO] Generating PDF report..."

python analytics/pdf_reports/generate_pdf_report.py

echo "[INFO] PDF reporting completed."
