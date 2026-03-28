# throughput.py

def validate_throughput(throughput, threshold=50000):
    if throughput >= threshold:
        print("Throughput validation PASSED")
    else:
        print("Throughput validation FAILED")