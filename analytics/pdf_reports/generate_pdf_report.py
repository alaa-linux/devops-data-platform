from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd
from sqlalchemy import create_engine

output_path = "analytics/pdf_reports/data_analysis_report.pdf"

engine = create_engine(
    "postgresql+psycopg2://warehouse_user:warehouse_password@localhost:5432/warehouse"
)

kpi_df = pd.read_sql("SELECT * FROM vw_kpi_alerts", engine)

c = canvas.Canvas(output_path, pagesize=A4)
width, height = A4

c.setFont("Helvetica-Bold", 18)
c.drawString(50, height - 60, "Data Analysis Report")

c.setFont("Helvetica", 12)
c.drawString(50, height - 100, "Projet : DevOps Data Platform")
c.drawString(50, height - 120, "Etape 138 : Rapport PDF automatique")

c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 170, "KPI Alerts")

y = height - 210

c.setFont("Helvetica", 11)

for _, row in kpi_df.iterrows():
    line = f"{row['kpi_name']} | value={row['kpi_value']} | status={row['alert_status']}"
    c.drawString(50, y, line)
    y -= 20

c.setFont("Helvetica-Bold", 14)
c.drawString(50, y - 30, "Analyse")

c.setFont("Helvetica", 11)
c.drawString(50, y - 60, "Les revenus sont fortement domines par les ventes Laptop.")
c.drawString(50, y - 80, "Des anomalies critiques sont detectees sur les revenus eleves.")
c.drawString(50, y - 100, "Les doublons depassent le seuil critique defini.")
c.drawString(50, y - 120, "La plateforme reste stable cote performance systeme.")



c.save()

print(f"PDF generated with KPI: {output_path}")
