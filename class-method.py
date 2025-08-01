from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # cls here refers to the 'Person' class
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)  # Calls the __init__ of the class (Person)


# Standard way to create an instance
person1 = Person("Alice", 30)
print(person1)  # Output: Person(name='Alice', age=30)

# Using the class method as an alternative constructor
person2 = Person.from_birth_year("Bob", 1990)
print(person2)  # Output: Person(name='Bob', age=35) (assuming current_year is 2025)


# Benefit with inheritance:
class Employee(Person):
    def __init__(self, name, age, employee_id=None):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __repr__(self):
        return f"Employee(name='{self.name}', age={self.age}, id={self.employee_id})"


# If you use Person.from_birth_year it would return a Person object.
# But using cls in the class method ensures it returns an Employee object
# when called on the Employee class.
employee1 = Employee.from_birth_year("Carol", 1985)
print(employee1)  # Output: Employee(name='Carol', age=40, id=None)
# Note: employee_id is None because our simple example doesn't pass it.
# A more robust factory method would handle all parameters.
