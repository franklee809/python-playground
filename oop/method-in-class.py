class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("Called static method")


# ClassTest.instance_method(ClassTest())
# ClassTest.class_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book :{self.name}, type: {self.book_type}, weighing :{self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 100)


print(Book("test", "hardcover", 123123))
print(Book.hardcover("test", 123123))
print(Book.paperback("test paperback", 1232))
