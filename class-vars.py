class MyClass:
    class_var = "I am a class variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var

    def my_method(self):
        pass


obj = MyClass("I am an instance variable")
print(vars(obj))
print(vars(MyClass))
print(dir(obj))
# print(dir(MyClass))
