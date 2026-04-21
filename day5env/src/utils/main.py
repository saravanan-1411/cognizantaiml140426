#display customers
import sys
import os
 
# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
 
sys.path.append(project_root)
from configuration.conf import Config
from dataloaders.customer_json_data_loader import CustomerJSONDataLoader
from dataloaders.customer_txt_data_loader import CustomerTXTDataLoader
from dataloaders.customer_csv_data_loader import CustomerCSVDataLoader
from stores.customer_store_impl import CustomerStoreImpl
def display_customers(customer_store):
    config=Config()
    env=config.app_env
    print(f"Running in {env} environment")
    if env == "Production":
        data_loader = CustomerJSONDataLoader()
        print(f"Loading data from {config.resource_path} for {env} environment")
        data_loader.load_data(config.resource_path, customer_store)
        for customer in customer_store.get_all_customers():
            print(customer)
    elif env == "Development":
        data_loader = CustomerCSVDataLoader()
        print(f"Loading data from {config.resource_path} for {env} environment")
        data_loader.load_data(config.resource_path, customer_store)
        for customer in customer_store.get_all_customers():
            print(customer)
    elif env == "Testing":
        data_loader = CustomerTXTDataLoader()
        print(f"Loading data from {config.resource_path} for {env} environment")
        data_loader.load_data(config.resource_path, customer_store)
        for customer in customer_store.get_all_customers():
            print(customer)

if __name__ == "__main__":
    customer_store = CustomerStoreImpl()
    display_customers(customer_store)