from contextlib import contextmanager
import time

@contextmanager
def timer_context():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Amal bajarish uchun {elapsed_time:.6f} sekund sarflandi.")

with timer_context():
    result = 1
    for i in range(1, 100001):
        result *= i


