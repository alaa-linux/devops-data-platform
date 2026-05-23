import json
import logging
import sys
from datetime import datetime
from pathlib import Path

import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError, RequestException


API_URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = {
    "latitude": 43.2965,
    "longitude": 5.3698,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "Europe/Paris"
}

LOG_DIR = Path("logs/ingestion")
LOG_FILE = LOG_DIR / "weather_api.log"


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


def extract_weather_data():
    try:
        logging.info("Début appel API Open-Meteo")

        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "current" not in data:
            raise ValueError("Champ 'current' absent de la réponse API")

        logging.info("Données météo récupérées avec succès")
        return data

    except Timeout:
        logging.exception("Timeout lors de l'appel API")
        raise

    except ConnectionError:
        logging.exception("Impossible de se connecter à l'API")
        raise

    except HTTPError as error:
        logging.exception("Erreur HTTP: %s", error)
        raise

    except ValueError as error:
        logging.exception("Erreur JSON/validation: %s", error)
        raise

    except RequestException as error:
        logging.exception("Erreur requête API: %s", error)
        raise


def save_raw_data(data):
    output_dir = Path("datasets/raw/weather")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"open_meteo_{timestamp}.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    logging.info("Données brutes sauvegardées dans %s", output_file)
    return output_file


def main():
    setup_logging()
    logging.info("Pipeline ingestion météo démarré")

    try:
        weather_data = extract_weather_data()
        saved_file = save_raw_data(weather_data)
        logging.info("Pipeline ingestion météo terminé avec succès: %s", saved_file)

    except Exception:
        logging.exception("Pipeline ingestion API échoué")
        sys.exit(1)


if __name__ == "__main__":
    main()
