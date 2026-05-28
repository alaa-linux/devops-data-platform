# Dashboard Datasets — Étape 124

## Objectif

Ce rapport documente les datasets préparés pour les futurs dashboards analytiques.

---

## Datasets SQL disponibles

| Dataset | Source |
|---|---|
| KPI globaux | vw_sales_global_kpi |
| Revenu par produit | vw_revenue_by_product |
| Revenu par ville | vw_revenue_by_city |
| Ventes journalières | vw_sales_daily |
| Incidents plateforme | vw_incidents |
| Performance plateforme | vw_performance |
| Airflow jobs | vw_airflow_jobs |
| Kafka metrics | vw_kafka_metrics |
| Spark jobs | vw_spark_jobs |

---

## Exports CSV générés

| Export | Fichier |
|---|---|
| Revenu par produit | analytics/dashboard/exports/revenue_by_product.csv |
| Revenu par ville | analytics/dashboard/exports/revenue_by_city.csv |
| Ventes journalières | analytics/dashboard/exports/sales_daily.csv |

---

## Utilisation

Ces datasets peuvent être consommés par :

- Apache Superset
- Grafana
- Power BI
- Metabase
- Excel
- Notebooks pandas
- APIs analytiques

---

## Conclusion

Les premiers datasets dashboard ont été préparés et exportés avec succès.

Statut : Étape 124 validée.
