import os

SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "change_me_superset_secret_key")

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SUPERSET_METADATA_DB_URI",
    "sqlite:////app/superset_home/superset.db"
)
