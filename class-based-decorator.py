from icecream import ic 
import time
from pprint import pprint


# class based decorator example for teaching purpose
class Call_Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1  # Bezug auf das Objekt selbst
        print(f"[Call_Counter] {self.func.__name__} has been called {self.count} times.")
        print(f"[Call_Counter] Arguments: args= {args}, kwargs ={kwargs}")
        return self.func(*args, **kwargs)


class Cache:
    def __init__(self, func):
        self.func = func
        self.history = []
        self.cache = {}
        ic("init")

    def __call__(self, *args, **kwargs):
        ic("call")
        key=(args, frozenset(kwargs.items()))
        ic(kwargs.items())
        ic (frozenset(kwargs.items()))
        ic (list(frozenset(kwargs.items())))
        ic(key)
        if key in self.cache:
            self.history.append(("cache",args, kwargs, self.cache[key]))
            return self.cache[key]
        
        else:
            result = self.func(*args, **kwargs)
            self.cache[key] = result
            self.history.append(("calc", args, kwargs, result))
            return result



@Cache
def complicated_calculation(x, comment = "No comment"):
    print(f"Performing complicated calculation for {x}...")
    time.sleep(2)
    return x * x


@Cache
def complicated_calculation_2(x, comment = "No comment"):
    print(f"Performing complicated calculation 2 for {x}...")
    time.sleep(2)
    return x * x



result = complicated_calculation(5)
print(f"Result: {result}")
result = complicated_calculation(6)
print(f"Result: {result}")
result = complicated_calculation(7)
print(f"Result: {result}")
result = complicated_calculation(5)
print(f"Result: {result}")
result = complicated_calculation(6)
print(f"Result: {result}")
result = complicated_calculation(7)
print(f"Result: {result}")
result = complicated_calculation(8)
print(f"Result: {result}")

result = complicated_calculation(10)
print(f"Result: {result}")

result = complicated_calculation_2(50)
print(f"Result: {result}")

result = complicated_calculation_2(100)
print(f"Result: {result}")

print(f"History: ")
pprint(complicated_calculation.history)
pprint(complicated_calculation.cache)
print(f"History 2: {complicated_calculation_2.history}")
