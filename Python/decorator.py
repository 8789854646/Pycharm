
# def positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return abs(result)
#     return wrapper
#
# @positive
# def sub(a, b):
#     return a-b
#
# print(sub(8, 15))


# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"You are calling {func.__name__}")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @log
# def spam():
#     return "hello world"
# @log
# def greet(name):
#     return f"hello world"
#
# print(greet("vivek"))
# print(spam())