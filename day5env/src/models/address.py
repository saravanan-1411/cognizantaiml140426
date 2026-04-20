#create address class associated to customer using pydantic
from pydantic import BaseModel, Field
from modelcustomer import Customer
class Address(BaseModel):
    customer:Customer
    street:str=Field(...,min_length=2, max_length=100, description="Street address")
    city:str=Field(...,min_length=2, max_length=100, description="City")
    state:str=Field(...,min_length=2, max_length=100, description="State")
    zip_code:str=Field(...,min_length=5, max_length=10, description="Zip code")
    country:str=Field(...,min_length=2, max_length=50, description="Country name")