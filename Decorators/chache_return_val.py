import time

def cache(func):
    cache_value = {}
    # print(f"{k},{v}")
    print(cache_value)
    def wrapper(*args):
        if args is cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def lng_running_func(a,b):
    time.sleep(4)
    return a + b


print(lng_running_func(2,3))
print(lng_running_func(2,3))
print(lng_running_func(4,3))