# Superset Installation — Étape 126

## Objectif

Cette étape documente l'installation de Apache Superset pour la couche BI / Dashboarding.

---

## Structure créée

| Élément | Description |
|---|---|
| dashboards/superset/config | Configuration Superset |
| dashboards/superset/data | Données persistantes |
| docker-compose-superset.yml | Déploiement Docker Superset |

---

## Configuration Superset

Fichier :

dashboards/superset/config/superset_config.py

Configuration utilisée :

- SECRET_KEY
- FEATURE_FLAGS
- SQLALCHEMY_DATABASE_URI

---

## Déploiement Docker

Container :

superset

Port exposé :

8088

Commande utilisée :

docker compose -f docker-compose-superset.yml up -d

---

## Validation Docker

Commande :

docker ps

Résultat :

- container Superset démarré ;
- état healthy ;
- port 8088 exposé.

---

## Initialisation admin

Commande utilisée :

docker exec -it superset superset fab create-admin

Utilisateur créé :

- username : admin

---

## Validation Web

URL validée :

http://localhost:8088

Validation :

- interface accessible ;
- authentification fonctionnelle ;
- dashboards/charts/datasets visibles.

---

## Conclusion

Apache Superset a été installé et validé avec succès.

Statut : Étape 126 validée.
