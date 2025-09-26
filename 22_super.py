from typing import override


class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I'm {self.age} years old.")


class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        super().__init__(name, age)
        self.student_id: int = student_id

    @override
    def greet(self):
        print(
            f"Hi, my name is {self.name} and I'm {self.age} years old. My student ID is {self.student_id}."
        )


st = Student("Ana", 20, 12345)
st.greet()
