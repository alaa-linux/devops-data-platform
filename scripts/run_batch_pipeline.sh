#!/bin/bash

set -e

echo "=== Exécution du pipeline batch Spark ==="

docker exec spark-master /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  /opt/spark/jobs/batch_sales_pipeline_job.py

echo "=== Lecture et validation des sorties batch ==="

docker exec spark-master /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  /opt/spark/jobs/read_batch_outputs_job.py

echo "=== Pipeline batch terminé avec succès ==="
