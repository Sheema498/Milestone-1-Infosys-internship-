import json
import random
from datetime import datetime

services = ["auth", "payment", "orders"]

def generate_log():
    return {
        "timestamp": str(datetime.now()),
        "level": random.choice(["INFO", "WARNING", "ERROR"]),
        "service": random.choice(services),
        "message": random.choice([
            "Login success",
            "Payment failed",
            "Database timeout",
            "Order placed"
        ])
    }

def generate_logs(file="logs.json", count=50):
    with open(file, "w") as f:
        for _ in range(count):
            f.write(json.dumps(generate_log()) + "\n")

if __name__ == "__main__":
    generate_logs()
    print("Logs generated!")
