#create class individual using pydantic
from pydantic import Field
from datetime import date
from pydantic import Fieldvalidator
from modelcustomer import Customer
from model.gender import Gender
class Individual(Customer):
    gender: Gender  
    dob: date =Field(..., description="Date of birth in yyyy-mm-dd format")

    @FieldValidator('dob')
    def validate_dob(cls, value):
        if value >= date.today():
            raise ValueError("Date of birth must be in the past")
        age = (date.today() - value).days // 365
        if age < 18:
            raise ValueError("Customer must be at least 18 years old")
        return value