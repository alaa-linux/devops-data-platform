# RAW Data

Ce dossier contient les données brutes collectées par les pipelines d’ingestion.

## Principe

Les données RAW sont sauvegardées sans transformation afin de conserver une copie fidèle de la source originale.

## Source actuelle

- Open-Meteo API

## Format

- JSON brut
- nommage avec timestamp

## Exemple

open_meteo_YYYYMMDD_HHMMSS.json

## Champs principaux

- latitude
- longitude
- timezone
- current.time
- temperature_2m
- relative_humidity_2m
- wind_speed_10m

## Usage futur

Ces fichiers seront utilisés par :

- Spark
- Data Lake
- ETL
- PostgreSQL Warehouse
- Data Analysis
- Machine Learning
