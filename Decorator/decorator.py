import time

def timeit(function):
    def inner(a,b):
        start_time = time.time()
        res = function(a, b)
        end_time = time.time()
        print(f"Total time elapsed: {(end_time - start_time)*1000}")
        return res
    return inner

@timeit
def division(a, b):
    time.sleep(2)
    return a / b

result = division(5,3)
print(f"{result=}")