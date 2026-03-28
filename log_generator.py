# log_generator.py

import pandas as pd
import random
import os
from datetime import datetime, timedelta
from config import LOG_FILE_PATH, NUM_LOGS

LOG_LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]
SERVICES = ["auth-service", "payment-service", "user-service", "order-service"]

def generate_logs():
    os.makedirs("sample_logs", exist_ok=True)
    
    base_time = datetime.now()
    data = []

    for i in range(NUM_LOGS):
        log = {
            "timestamp": (base_time + timedelta(seconds=i)).isoformat(),
            "log_level": random.choice(LOG_LEVELS),
            "service": random.choice(SERVICES),
            "message": f"Log message {i}",
            "response_time": round(random.uniform(0.1, 5.0), 3)
        }
        data.append(log)

    df = pd.DataFrame(data)
    df.to_csv(LOG_FILE_PATH, index=False)
    print(f"Generated {NUM_LOGS} logs successfully.")