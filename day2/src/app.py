# create a entry point for the application
import faker
from store.customer_store import CustomerStore
from view.customer_view import CustomerView
"""
This is the main entry point for the application. It creates an instance of the CustomerStore class and the CustomerView class, and calls the display_customers method to display the customer details.
"""


def run():
    """
    This function creates an instance of the CustomerView class and calls the display_customers method to display the customer details
    """
    customer_store = CustomerStore(num_customers=100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()



if __name__ == "__main__":
    run()
