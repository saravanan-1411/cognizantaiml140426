import typing
import datetime
class customer:
    def __init__(self, name: str, age: int, email: str, phone: str, address: str, registration_date: datetime.date):
        self.name = name
        self.age = age
        self.email = email
        self.dob =dob

    def __str__(self):
        return f"Customer(name={self.name}, age={self.age}, email={self.email}, dob={self.dob})"