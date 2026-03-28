import ray
import dask.dataframe as dd
import pandas as pd

def test_ray():
    print("Starting Ray...")
    ray.init(ignore_reinit_error=True)

    @ray.remote
    def square(x):
        return x * x

    futures = [square.remote(i) for i in range(5)]
    results = ray.get(futures)

    print("Ray Output:", results)


def test_dask():
    print("Starting Dask...")
    df = pd.DataFrame({"numbers": range(10)})
    ddf = dd.from_pandas(df, npartitions=2)

    print("Dask partitions:", ddf.npartitions)
    print(ddf.compute())


if __name__ == "__main__":
    test_ray()
    test_dask()
