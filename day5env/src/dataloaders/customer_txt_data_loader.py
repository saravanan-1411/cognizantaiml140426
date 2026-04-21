import pandas as pd
from dataloaders.customer_data_loader import CustomerDataLoader
from stores.customer_store_impl import CustomerStoreImpl
from models.customer import Customer
from models.full_name import FullName

class CustomerTXTDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return

        # Split records by blank lines
        records = content.strip().split("\n\n")

        for record in records:
            lines = record.strip().split("\n")
            data = {}

            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    data[key.strip()] = value.strip()

            try:
                customer_id = int(data.get('customer_id'))
                first_name = data.get('first_name', "")
                last_name = data.get('last_name', "")
                email = data.get('email', "")
                phone_no = data.get('phone_no', "")

                full_name = FullName(first_name=first_name, last_name=last_name)
                customer = Customer(
                    customer_id=customer_id,
                    name=full_name,
                    email=email,
                    phone_no=phone_no
                )
                customer_store.add_customer(customer)

            except (TypeError, ValueError) as e:
                print(f"Skipping invalid record: {record}\nError: {e}")
