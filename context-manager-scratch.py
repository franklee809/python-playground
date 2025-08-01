### Class based context manager
# class HelloContextManager:
#     def __enter__(self):
#         print("Entering the context...")
#         return "Hello, World!"

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print("Leaving the context。。。")
#         # print(exc_type, exc_value, exc_tb, sep="\n")
#         if exc_type is ZeroDivisionError:
#             print("triggered")


# with HelloContextManager() as message:
#     1 / 0
#     print(message)


### Write file context manager
# class WritableFile:
#     def __init__(self, file_path):
#         self.file_path = file_path

#     def __enter__(self):
#         self.file_obj = open(self.file_path, mode="w")
#         return self.file_obj

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         if self.file_obj:
#             self.file_obj.close()


# with WritableFile("hello.txt") as file:
#     file.write("hello world!")


### Redirecting the standard output

# import sys


# class RedirectedStdout:
#     def __init__(self, new_output):
#         self.new_output = new_output
#         print("newoutput", new_output)

#     def __enter__(self):
#         # 1. Save the original standard output (the console)
#         self.saved_output = sys.stdout
#         print("std out", sys.stdout)
#         # 2. This is the line that redirects stdout to the file object
#         sys.stdout = self.new_output

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         # 4. Restore the original standard output when exiting the 'with' block
#         sys.stdout = self.saved_output


# with open("hello.txt", "w") as file:
#     with RedirectedStdout(file):
#         # 3. These print statements now write to "hello.txt"
#         print("🚀 ~ file:", file)
#         print("hello world! 1231231")
#     # 5. Now that we've exited the inner 'with' block, this prints to the console again
#     print("back to the standard output")

from time import perf_counter, sleep


class Timer:
    def __init__(self):
        self.elapsed = 0.0

    def __enter__(self):
        self.start = perf_counter()
        return self  # Return the instance itself

    def __exit__(self, *args):
        self.end = perf_counter()
        self.elapsed = self.end - self.start


with Timer() as timer:  # 'timer' is now the Timer instance
    # Time-consuming code goes here
    sleep(0.5)

print(f"Elapsed time: {timer.elapsed:.4f} seconds")
