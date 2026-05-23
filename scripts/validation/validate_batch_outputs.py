from pathlib import Path
import sys

base_path = Path("/opt/spark/data/output/batch")

required_datasets = [
    "clean_sales",
    "global_kpi",
    "revenue_by_city",
    "revenue_by_product"
]

errors = []

for dataset in required_datasets:
    dataset_path = base_path / dataset

    if not dataset_path.exists():
        errors.append(f"{dataset} introuvable")
        continue

    success_file = dataset_path / "_SUCCESS"

    if not success_file.exists():
        errors.append(f"{dataset} sans fichier _SUCCESS")

    parquet_files = list(dataset_path.glob("*.parquet"))

    if len(parquet_files) == 0:
        errors.append(f"{dataset} sans fichier parquet")

if errors:
    print("Validation échouée")
    for err in errors:
        print(f"ERREUR : {err}")
    sys.exit(1)

print("Validation batch Spark réussie")
