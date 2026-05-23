import json
import logging
import sys
from datetime import datetime
from pathlib import Path

from kafka import KafkaConsumer


TOPIC_NAME = "sales-topic"
BOOTSTRAP_SERVERS = "localhost:9092"

OUTPUT_DIR = Path("processing/streaming/output/sales")
OUTPUT_FILE = OUTPUT_DIR / "sales_events.jsonl"

LOG_DIR = Path("logs/kafka")
LOG_FILE = LOG_DIR / "realtime_sales_pipeline.log"


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
        group_id="realtime-sales-pipeline",
        value_deserializer=lambda value: json.loads(value.decode("utf-8")),
    )


def transform_event(event):
    quantity = int(event["quantity"])
    price = float(event["price"])

    event["quantity"] = quantity
    event["price"] = price
    event["total_amount"] = quantity * price
    event["processed_at"] = datetime.now().isoformat()

    return event


def save_event(event):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event, ensure_ascii=False) + "\n")


def run_pipeline():
    consumer = create_consumer()

    logging.info("Pipeline temps réel connecté au topic: %s", TOPIC_NAME)

    for message in consumer:
        raw_event = message.value
        transformed_event = transform_event(raw_event)
        save_event(transformed_event)

        logging.info("Événement traité et sauvegardé: %s", transformed_event)


def main():
    setup_logging()
    logging.info("Pipeline temps réel sales démarré")

    try:
        run_pipeline()

    except KeyboardInterrupt:
        logging.info("Pipeline arrêté manuellement")

    except Exception:
        logging.exception("Pipeline temps réel sales échoué")
        sys.exit(1)


if __name__ == "__main__":
    main()
