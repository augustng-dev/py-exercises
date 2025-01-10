import time

def measure_execution_time():
    start = time.time()
    for _ in range(10000):
        1 + 1
    end = time.time()
    return f"Execution Time: {end - start} seconds"

# Example usage
print(measure_execution_time())