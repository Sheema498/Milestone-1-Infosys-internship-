# ray_pipeline.py
import numpy as np
import ray
import pandas as pd
import time
from parser import parse_log
from config import LOG_FILE_PATH, RAY_NUM_WORKERS

@ray.remote
def process_chunk(chunk):
    return chunk.apply(parse_log, axis=1)

def process_with_ray():
    print("Starting Ray processing...")

    ray.init(ignore_reinit_error=True)

    start_time = time.time()

    df = pd.read_csv(LOG_FILE_PATH)
    chunks = np.array_split(df, RAY_NUM_WORKERS)

    futures = [process_chunk.remote(chunk) for chunk in chunks]
    results = ray.get(futures)

    final_result = pd.concat(results)

    end_time = time.time()

    total_time = end_time - start_time
    throughput = len(final_result) / total_time

    print(f"Ray Processing Time: {total_time:.2f} seconds")
    print(f"Ray Throughput: {throughput:.2f} logs/sec")

    ray.shutdown()

    return final_result