import json
from datetime import datetime
from pathlib import Path

output_dir = Path("/opt/data/raw/api")
output_dir.mkdir(parents=True, exist_ok=True)

records = [
    {
        "date": "2026-05-16",
        "product": "Laptop",
        "quantity": 1,
        "price": 1200,
        "city": "Marseille",
        "source": "mock_api"
    },
    {
        "date": "2026-05-16",
        "product": "Phone",
        "quantity": 2,
        "price": 900,
        "city": "Paris",
        "source": "mock_api"
    }
]

output_file = output_dir / f"sales_api_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with output_file.open("w", encoding="utf-8") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)

print(f"Ingestion terminée : {output_file}")
