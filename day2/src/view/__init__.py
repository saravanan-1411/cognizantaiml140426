#show customer details
from store.customerstore import CustomerStore
class CustomerView:
    def __init__(self, num_customers: int):
        self.customers=[]

    def display_customers(self):
        customers = self.customer_store.get_customers()
        for customer in customers:
            print(customer)