#generate 100 customers
import faker
import typing
from models.customer import Customer
class CustomerStore:
    def __init__(self):
        self.customers = []
        self.generate_customers()

    def generate_customers(self):
        faker = faker.Faker()
        for _ in range(n):
            name = faker.name()
            email = faker.email()
            dob = faker.date_of_birth()
            customer = Customer(name, email, dob)
            self.customers.append(customer)

    def get_customers(self) -> typing.List[Customer]:
        return self.customers