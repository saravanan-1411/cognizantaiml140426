#create customer csv data loader implementation from 
import pandas as pd
from dataloaders.customer_data_loader import CustomerDataLoader
from stores.customer_store_impl import CustomerStoreImpl
from models.full_name import FullName
from models.customer import Customer
class CustomerCSVDataLoader(CustomerDataLoader):
    def load_data(self,file_path,customer_store:CustomerStoreImpl):
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            customer_id=int(row['customer_id'])
            first_name=row['first_name']
            last_name=row['last_name']
            email=row['email']
            phone_no=int(row['phone_no'])
            full_name = FullName(first_name=first_name, last_name=last_name)
            customer = Customer(customer_id=customer_id, name=full_name, email=email, phone_no=phone_no)
            customer_store.add_customer(customer)
