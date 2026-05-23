# Sources de données du projet

## Objectif

Ce document définit les sources de données utilisées dans la plateforme DevOps Data Platform.

Le projet utilise plusieurs familles de données afin de couvrir :

- Data Engineering
- Data Analysis
- Data Science
- Machine Learning
- IA / NLP
- Observabilité DevOps
- Streaming temps réel

---

## 1. APIs publiques

Les APIs publiques seront utilisées pour récupérer des données JSON structurées.

### Exemple principal

- Open-Meteo API

### Usage

- ingestion API
- stockage JSON brut
- transformation Spark
- chargement warehouse
- dashboards analytiques
- modèles prédictifs simples

---

## 2. Fichiers CSV

Les fichiers CSV serviront aux analyses batch.

### Types prévus

- ventes
- transactions
- IoT
- événements applicatifs
- datasets publics

### Usage

- Data Analyst
- SQL Analytics
- Machine Learning
- rapports
- dashboards

---

## 3. Logs système Linux

Les logs Linux seront utilisés pour la partie observabilité et IA appliquée aux incidents.

### Exemples

- logs apt
- logs dpkg
- logs système disponibles dans /var/log

### Usage

- analyse d'événements système
- détection anomalies
- NLP logs
- classification incidents

---

## 4. Logs Docker / Kubernetes

Ces logs seront ajoutés progressivement.

### Docker

Disponible dès les premiers conteneurs.

### Kubernetes

Disponible plus tard dans le Bloc G.

### Usage

- supervision
- troubleshooting
- alerting
- analyse incidents

---

## 5. Données streaming simulées

Des événements seront générés pour simuler un flux temps réel.

### Exemples

- métriques CPU
- événements applicatifs
- logs simulés
- transactions simulées

### Usage

- Kafka
- Spark Streaming
- monitoring temps réel
- anomalies ML

---

## Conclusion

La plateforme ne dépend pas uniquement de Kubernetes.

Les phases Data Engineering, Data Analyst, Data Science, ML et IA peuvent commencer avec :

- APIs
- CSV
- logs Linux
- données simulées

Kubernetes servira plus tard à industrialiser et déployer la plateforme.
