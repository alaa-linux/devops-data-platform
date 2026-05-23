import csv
import logging
import shutil
import sys
from datetime import datetime
from pathlib import Path


SOURCE_FILE = Path("datasets/csv/sales_data.csv")
RAW_DIR = Path("datasets/raw/sales")
LOG_DIR = Path("logs/ingestion")
LOG_FILE = LOG_DIR / "sales_csv.log"


def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(sys.stdout)
        ]
    )


def validate_csv_file(file_path):
    if not file_path.exists():
        raise FileNotFoundError(f"Fichier CSV introuvable: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("Le fichier CSV ne contient aucune donnée")

    required_columns = {"date", "product", "quantity", "price", "city"}

    if set(reader.fieldnames) != required_columns:
        raise ValueError(f"Colonnes invalides: {reader.fieldnames}")

    logging.info("CSV validé avec succès: %s lignes", len(rows))
    return rows


def save_raw_csv(source_file):
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = RAW_DIR / f"sales_data_{timestamp}.csv"

    shutil.copy2(source_file, output_file)

    logging.info("CSV brut sauvegardé dans %s", output_file)
    return output_file


def main():
    setup_logging()
    logging.info("Pipeline ingestion CSV démarré")

    try:
        validate_csv_file(SOURCE_FILE)
        saved_file = save_raw_csv(SOURCE_FILE)
        logging.info("Pipeline ingestion CSV terminé avec succès: %s", saved_file)

    except Exception:
        logging.exception("Pipeline ingestion CSV échoué")
        sys.exit(1)


if __name__ == "__main__":
    main()
