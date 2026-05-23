import csv
import json
import logging
import sys
import time
from pathlib import Path

from kafka import KafkaProducer
from kafka.errors import KafkaError


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
        retries=5,
        retry_backoff_ms=1000,
        request_timeout_ms=30000,
        acks="all",
    )


def read_sales_events():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Fichier CSV introuvable: {CSV_FILE}")

    with CSV_FILE.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def send_event_with_retry(producer, event):
    try:
        future = producer.send(TOPIC_NAME, value=event)
        metadata = future.get(timeout=10)

        logging.info(
            "Message envoyé vers %s | partition=%s | offset=%s | event=%s",
            metadata.topic,
            metadata.partition,
            metadata.offset,
            event,
        )

    except KafkaError as error:
        logging.exception("Erreur Kafka pendant l'envoi du message: %s", error)
        raise


def send_events():
    producer = create_producer()
    events = read_sales_events()

    try:
        for event in events:
            send_event_with_retry(producer, event)
            time.sleep(1)

        producer.flush()
        logging.info("Tous les messages sales ont été envoyés")

    finally:
        producer.close()


def main():
    setup_logging()
    logging.info("Producer Kafka sales avec retry démarré")

    try:
        send_events()
        logging.info("Producer Kafka sales terminé avec succès")

    except Exception:
        logging.exception("Producer Kafka sales échoué")
        sys.exit(1)


if __name__ == "__main__":
    main()
