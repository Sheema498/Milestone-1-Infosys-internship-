# config.py

import os

# Log file path
LOG_FILE_PATH = "sample_logs\logs.csv"

# Number of logs to generate
NUM_LOGS = 1_000_000

# Dask Config
DASK_PARTITIONS = 4

# Ray Config
RAY_NUM_WORKERS = 4

# Schema definition
LOG_SCHEMA = {
    "timestamp": "str",
    "log_level": "str",
    "service": "str",
    "message": "str",
    "response_time": "float"
}