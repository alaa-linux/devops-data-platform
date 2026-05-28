# SQL Reports Results — Étape 125

## Objectif

Ce rapport documente les rapports SQL créés pour la couche Data Analyst.

---

## Rapports SQL créés

| Fichier | Objectif |
|---|---|
| analytics/sql_reports/incidents_report.sql | Rapport incidents |
| analytics/sql_reports/performance_report.sql | Rapport performance |
| analytics/sql_reports/airflow_report.sql | Rapport Airflow |
| analytics/sql_reports/kafka_report.sql | Rapport Kafka |
| analytics/sql_reports/spark_report.sql | Rapport Spark |
| analytics/sql_reports/exports/metrics_report.csv | Export CSV metrics |
| analytics/sql_reports/run_sql_reports.sh | Automatisation rapports SQL |

---

## Validation

Les rapports SQL ont été exécutés avec succès via :

bash analytics/sql_reports/run_sql_reports.sh

---

## Résultat

Le script a exécuté les rapports suivants :

- incidents ;
- performance ;
- Airflow ;
- Kafka ;
- Spark.

---

## Conclusion

Les rapports SQL de l'étape 125 ont été créés, exportés, automatisés et validés.

Statut : Étape 125 validée.
