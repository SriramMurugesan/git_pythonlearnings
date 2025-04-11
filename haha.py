# def add(a, b):
#     return a + b


# def add_all(*args):
#     return sum(args)

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# def add(a=0, b=0):
#     return a + b
# print(add())

# def demo(*args, **kwargs):
#     print("ARGS:", args)
#     print("KWARGS:", kwargs)

# demo(1, 2, 3, name="Alex", age=25)

# def smart_func(*args, **kwargs):
#     total = sum(args)
#     print("Sum of args:", total)
#     for k, v in kwargs.items():
#         print(f"{k} = {v}")

# smart_func(10, 20, 30, name="Python", level="Advanced")

# def show_args(*args):
#     for i, val in enumerate(args):
#         print(f"Argument {i+1}: {val}")

# show_args("apple", 42, True)

# def logger(func):# List comprehension
# squares = [x**2 for x in range(10)]

# # Dict comprehension
# sqr_map = {x: x**2 for x in range(5)}

# # Set comprehension
# unique = {x for x in [1, 2, 2, 3, 3]}

# # Generator expression
# sqr_gen = (x**2 for x in range(10))

# print(squares)
# print(sqr_map)
# print(unique)
# print(sqr_gen)

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
finally:
    print("Done")

class MyError(Exception):
    pass

try:
    raise MyError("This is an error")
except MyError as e:
    print(e)

