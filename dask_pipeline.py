# dask_pipeline.py

import dask.dataframe as dd
import pandas as pd
import time
from parser import parse_log
from config import LOG_FILE_PATH, DASK_PARTITIONS


def apply_parse(df_partition):
    """
    Apply parse_log row-wise to a pandas partition.
    Returns a pandas DataFrame (NOT Series).
    """
    parsed_rows = df_partition.apply(parse_log, axis=1)
    return pd.DataFrame(list(parsed_rows))


def process_with_dask():
    print("Starting Dask processing...")

    start_time = time.time()

    # Read CSV
    df = dd.read_csv(LOG_FILE_PATH, blocksize="64MB")

    # Repartition
    df = df.repartition(npartitions=DASK_PARTITIONS)

    # Define metadata manually (VERY IMPORTANT)
    meta = pd.DataFrame({
        "timestamp": pd.Series(dtype="str"),
        "service": pd.Series(dtype="str"),
        "anomaly": pd.Series(dtype="bool")
    })

    # Map partitions with correct meta
    result = df.map_partitions(apply_parse, meta=meta)

    result = result.compute()

    end_time = time.time()

    total_time = end_time - start_time
    throughput = len(result) / total_time

    print(f"Dask Processing Time: {total_time:.2f} seconds")
    print(f"Dask Throughput: {throughput:.2f} logs/sec")

    return result