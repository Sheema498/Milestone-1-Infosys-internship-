# parser.py

from config import LOG_SCHEMA

def validate_schema(row):
    try:
        float(row["response_time"])
        return True
    except:
        return False

def parse_log(row):
    """
    Example parsing logic:
    - Detect anomaly if response_time > 4 sec
    - Detect error logs
    """
    anomaly = False

    if row["log_level"] == "ERROR":
        anomaly = True

    if float(row["response_time"]) > 4.0:
        anomaly = True

    return {
        "timestamp": row["timestamp"],
        "service": row["service"],
        "anomaly": anomaly
    }