from pathlib import Path

BASE_DIR = Path("/workspaces/FIFAWC26Pool").resolve()

# Core directories
DATA_DIR = BASE_DIR / "data"
TEMPLATES_DIR = BASE_DIR / "templates"
LOGS_DIR = BASE_DIR / "logs"

# Files
DB_PATH = DATA_DIR / "fifa_wc_2026_pool.db"
SCHEMA_PATH = TEMPLATES_DIR / "schema.sql"
LOG_FILE_PATH = LOGS_DIR / "wc_pool_logger.log"

# Create directories
for DIR in [DATA_DIR, LOGS_DIR]:
    if not DIR.exists():
        DIR.mkdir(parents=True, exist_ok=True)


if not SCHEMA_PATH.exists():
    raise FileNotFoundError("Schema file (schema.sql) not found.")
