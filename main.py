# main.py

from log_generator import generate_logs
from dask_pipeline import process_with_dask
from ray_pipeline import process_with_ray

def main():
    print("=== LOG INGESTION & DISTRIBUTED PROCESSING SYSTEM ===")

    # Step 1: Generate logs
    generate_logs()

    # Step 2: Process using Dask
    dask_results = process_with_dask()

    # Step 3: Process using Ray
    ray_results = process_with_ray()

    print("Processing Completed Successfully")

if __name__ == "__main__":
    main()
print("Hi, I'm Sheema")
