import csv
import json
import logging
import sys
import time
from pathlib import Path

from kafka import KafkaProducer


CSV_FILE = Path("datasets/csv/sales_data.csv")
TOPIC_NAME = "sales-topic"
BOOTSTRAP_SERVERS = "localhost:9092"

LOG_DIR = Path("logs/kafka")
LOG_FILE = LOG_DIR / "sales_producer.log"


def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def create_producer():
    return KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    )


def read_sales_events():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Fichier CSV introuvable: {CSV_FILE}")

    with CSV_FILE.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def send_events():
    producer = create_producer()
    events = read_sales_events()

    for event in events:
        producer.send(TOPIC_NAME, value=event)
        logging.info("Message envoyé vers %s: %s", TOPIC_NAME, event)
        time.sleep(1)

    producer.flush()
    producer.close()

    logging.info("Tous les messages sales ont été envoyés")


def main():
    setup_logging()
    logging.info("Producer Kafka sales démarré")

    try:
        send_events()
        logging.info("Producer Kafka sales terminé avec succès")

    except Exception:
        logging.exception("Producer Kafka sales échoué")
        sys.exit(1)


if __name__ == "__main__":
    main()
