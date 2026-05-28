# System Performance Analysis — Étape 136

## Objectif

Analyser les performances système de la plateforme DevOps Data Platform.

---

## CPU

Les containers les plus consommateurs CPU sont :

| Container | Observation |
|---|---|
| cadvisor | collecte métriques système |
| kibana | interface logs/observabilité |
| grafana | dashboards |
| elasticsearch | moteur indexation |
| kafka | broker messaging |

Conclusion CPU : aucune surcharge critique détectée.

---

## RAM

Mémoire système :

- RAM totale : 31 GiB
- RAM utilisée : environ 6.2 GiB
- RAM disponible : environ 25 GiB
- Swap utilisée : 0

Containers les plus consommateurs RAM :

| Container | Observation |
|---|---|
| elasticsearch | composant le plus lourd |
| cadvisor | monitoring Docker |
| kibana | interface observabilité |
| kafka | broker messaging |
| kafka-ui | interface Kafka |

Conclusion RAM : plateforme stable et non saturée.

---

## Kafka

Les logs Kafka montrent uniquement des opérations normales :

- preferred replica leader election ;
- auto leader balancing ;
- controller actif.

Conclusion Kafka : broker stable et opérationnel.

---

## Spark

Spark Master :

- service démarré sur 7077 ;
- UI démarrée sur 8080 ;
- leader élu ;
- worker enregistré.

Spark Worker :

- connecté au master ;
- 24 cores détectés ;
- 30.3 GiB RAM disponible.

Conclusion Spark : cluster Spark opérationnel.

---

## Airflow

Problème détecté :

Airflow tentait de se connecter au hostname incorrect :

postgres

Correction appliquée :

postgres → airflow-postgres

Services validés :

- airflow-webserver
- airflow-scheduler
- airflow-worker
- airflow-postgres
- airflow-redis

Conclusion Airflow : service corrigé et relancé avec succès.

---

## Conclusion générale

La plateforme est opérationnelle :

- CPU stable
- RAM stable
- Kafka opérationnel
- Spark opérationnel
- Airflow corrigé
- PostgreSQL opérationnel
- Superset opérationnel
- Monitoring actif

Statut : Étape 136 validée.
