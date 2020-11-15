from typing import TypedDict

# pylint: disable=inherit-non-class


class Student(TypedDict):
    id: str
    name: str
    age: int
