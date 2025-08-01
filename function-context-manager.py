### Function based context manager
from contextlib import contextmanager


# @contextmanager
# def writable_file(file_path):
#     file = open(file_path, mode="w")
#     try:
#         yield file
#     finally:
#         file.close()


# with writable_file("hello.txt") as file:
#     print("with before")
#     file.write("Hello World!")
#     print("with after")

from time import time


# @contextmanager
# def mock_time():
#     global time
#     saved_time = time
#     time = lambda: 42
#     yield
#     time = saved_time


# with mock_time():
#     print(f"time is {time()}")


### Text indentation level
class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.level -= 1

    def print(self, text):
        print(" " * self.level + text)


with Indenter() as indent:
    indent.print("hi!")
    with indent:
        indent.print("hello")
        with indent:
            indent.print("bonjour")
    indent.print("hey")
