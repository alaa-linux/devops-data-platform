# Business KPI — DevOps Data Platform

## Objectif

Ce document définit les premiers indicateurs KPI utilisés pour analyser la plateforme data.

Les KPI permettent de transformer les données techniques en indicateurs exploitables pour le suivi métier, opérationnel et analytique.

---

## KPI 1 — Chiffre d'affaires total

- Nom : Total Revenue
- Description : Somme totale du chiffre d'affaires généré par les ventes.
- Source : table ou vue analytique des ventes
- Formule : SUM(revenue)
- Usage : suivre la performance globale de l'activité.

---

## KPI 2 — Quantité totale vendue

- Nom : Total Quantity
- Description : Somme totale des quantités vendues.
- Source : table ou vue analytique des ventes
- Formule : SUM(quantity)
- Usage : mesurer le volume global de ventes.

---

## KPI 3 — Nombre total de ventes

- Nom : Total Sales Count
- Description : Nombre total de transactions ou lignes de vente.
- Source : table ou vue analytique des ventes
- Formule : COUNT(*)
- Usage : mesurer l'activité commerciale globale.

---

## KPI 4 — Chiffre d'affaires par produit

- Nom : Revenue By Product
- Description : Classement des produits selon leur chiffre d'affaires.
- Source : agrégation Spark / PostgreSQL
- Formule : SUM(revenue) GROUP BY product
- Usage : identifier les produits les plus performants.

---

## KPI 5 — Chiffre d'affaires par ville

- Nom : Revenue By City
- Description : Répartition du chiffre d'affaires par ville.
- Source : agrégation Spark / PostgreSQL
- Formule : SUM(revenue) GROUP BY city
- Usage : identifier les zones géographiques les plus rentables.

---

## KPI 6 — Qualité du pipeline

- Nom : Pipeline Success Rate
- Description : Pourcentage de traitements réussis.
- Source : Airflow / logs pipeline
- Formule : success_runs / total_runs * 100
- Usage : mesurer la fiabilité de la plateforme data.

---

## KPI 7 — Temps moyen de traitement

- Nom : Average Processing Time
- Description : Durée moyenne d'exécution des traitements batch ou streaming.
- Source : Airflow / Spark / logs
- Formule : AVG(duration)
- Usage : suivre la performance opérationnelle.

---

## KPI 8 — Erreurs applicatives

- Nom : Error Count
- Description : Nombre d'erreurs détectées dans les logs.
- Source : Elasticsearch / Filebeat / logs applicatifs
- Formule : COUNT(*) WHERE level = 'ERROR'
- Usage : détecter les incidents et instabilités.

---

## Statut

Première version des KPI business créée.
