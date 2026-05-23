import time
import requests
from prometheus_client import start_http_server, Gauge

SPARK_MASTER_URL = "http://spark-master:8080/json"
SPARK_WORKER_URL = "http://spark-worker-1:8081/json"

spark_master_alive_workers = Gauge("spark_master_alive_workers", "Number of alive Spark workers")
spark_master_cores_total = Gauge("spark_master_cores_total", "Total Spark cores")
spark_master_cores_used = Gauge("spark_master_cores_used", "Used Spark cores")
spark_master_memory_total_mb = Gauge("spark_master_memory_total_mb", "Total Spark memory in MB")
spark_master_memory_used_mb = Gauge("spark_master_memory_used_mb", "Used Spark memory in MB")
spark_master_apps_running = Gauge("spark_master_apps_running", "Running Spark applications")

spark_worker_cores = Gauge("spark_worker_cores", "Spark worker cores")
spark_worker_cores_used = Gauge("spark_worker_cores_used", "Spark worker used cores")
spark_worker_memory_mb = Gauge("spark_worker_memory_mb", "Spark worker memory in MB")
spark_worker_memory_used_mb = Gauge("spark_worker_memory_used_mb", "Spark worker used memory in MB")


def fetch_json(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        print(f"Error fetching {url}: {exc}")
        return {}


def collect_metrics():
    master = fetch_json(SPARK_MASTER_URL)

    if master:
        spark_master_alive_workers.set(master.get("aliveworkers", 0))
        spark_master_cores_total.set(master.get("cores", 0))
        spark_master_cores_used.set(master.get("coresused", 0))
        spark_master_memory_total_mb.set(master.get("memory", 0))
        spark_master_memory_used_mb.set(master.get("memoryused", 0))
        spark_master_apps_running.set(len(master.get("activeapps", [])) if isinstance(master.get("activeapps", []), list) else 0)

    worker = fetch_json(SPARK_WORKER_URL)

    if worker:
        spark_worker_cores.set(worker.get("cores", 0))
        spark_worker_cores_used.set(worker.get("coresused", 0))
        spark_worker_memory_mb.set(worker.get("memory", 0))
        spark_worker_memory_used_mb.set(worker.get("memoryused", 0))


if __name__ == "__main__":
    start_http_server(9400)
    print("Spark exporter started on port 9400")

    while True:
        collect_metrics()
        time.sleep(15)
