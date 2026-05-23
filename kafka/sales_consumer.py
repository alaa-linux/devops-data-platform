import json
import logging
import sys
from pathlib import Path

from kafka import KafkaConsumer


TOPIC_NAME = "sales-topic"
BOOTSTRAP_SERVERS = "localhost:9092"

LOG_DIR = Path("logs/kafka")
LOG_FILE = LOG_DIR / "sales_consumer.log"


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


def create_consumer():
    return KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="sales-consumer-group",
        value_deserializer=lambda value: json.loads(value.decode("utf-8")),
        consumer_timeout_ms=10000,
    )


def consume_events():
    consumer = create_consumer()

    message_count = 0

    for message in consumer:
        message_count += 1
        logging.info("Message reçu depuis %s: %s", TOPIC_NAME, message.value)

    consumer.close()
    logging.info("Nombre total de messages lus: %s", message_count)


def main():
    setup_logging()
    logging.info("Consumer Kafka sales démarré")

    try:
        consume_events()
        logging.info("Consumer Kafka sales terminé avec succès")

    except Exception:
        logging.exception("Consumer Kafka sales échoué")
        sys.exit(1)


if __name__ == "__main__":
    main()
