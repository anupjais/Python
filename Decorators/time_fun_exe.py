import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} run upto {end-start} time.")
        return result
    return wrapper

@timer
def example_func(n):
    time.sleep(n)

for i in range(10):
    example_func(i)