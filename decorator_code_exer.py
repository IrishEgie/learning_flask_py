# import time
# current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# # Write your code below 👇

# def speed_calc_decorator(func):
  
#   def wrapper(*args, **kwargs):
#     start_time = time.time()
#     result = func(*args, **kwargs)
#     end_time = time.time()
#     run_time = end_time - start_time
#     print(f"{func.__name__} run speed: {run_time}s")
#     return result
  
#   return wrapper

# @speed_calc_decorator
# def fast_function():
#   for i in range(1000000):
#     i * i
        
# @speed_calc_decorator
# def slow_function():
#   for i in range(10000000):
#     i * i

# fast_function()
# slow_function()


# --------------------- Exercise 2 -------------------------- #

def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}")
        result = func(*args)
        print(F"It returned: {result}")
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)