#create comfiguration for the project
import os
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

class Config:
    def __init__(self):
        self.app_env = os.getenv("APP_ENV")
        self.resource_path : str = self.get_resource_path()
    def get_resource_path(self) -> str:
        if self.app_env == "Production":
            return f"src/resources/customers.json"
        elif self.app_env == "Development":
            return f"src/resources/customers.csv"
        elif self.app_env == "Testing":
            return f"src/resources/customers.txt"
        else:
            raise ValueError(f"Invalid environment: {self.app_env}")