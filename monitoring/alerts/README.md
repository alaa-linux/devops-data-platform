# KPI Alerts — Étape 131

## Objectif

Cette étape définit et teste les alertes KPI liées à la qualité des données.

---

## Seuils configurés

| KPI | Warning | Critical |
|---|---:|---:|
| anomalies | > 10 | > 20 |
| duplicate_rows | > 50 | > 100 |
| total_nulls | > 0 | > 5 |
| ingestion_rows | - | < 100 |

---

## Fichiers créés

| Fichier | Rôle |
|---|---|
| monitoring/alerts/kpi_thresholds.yaml | Seuils KPI |
| monitoring/alerts/email_alerts_template.md | Template email |
| monitoring/alerts/grafana_alerts.md | Configuration alertes Grafana |
| monitoring/alerts/anomaly_alert_rules.sql | Règles SQL alertes |
| warehouse/sql/views/data_quality_views.sql | Vues SQL alerting |

---

## Résultat du test

Les alertes actives détectées sont :

| KPI | Valeur | Statut |
|---|---:|---|
| anomalies | 25 | CRITICAL |
| duplicate_rows | 180 | CRITICAL |

---

## Conclusion

Les alertes KPI ont été définies, configurées, testées et documentées.

Statut : Étape 131 validée.
