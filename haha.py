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

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}")

greet("Alice")


