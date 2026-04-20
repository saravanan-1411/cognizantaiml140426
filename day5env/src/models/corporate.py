#create corporate class inherit from customer using pydantic
from pydantic import Field
from modelcustomer import Customer
from model.company_type import CompanyType
class Corporate(Customer):
    company_type: CompanyType
    registration_number: str = Field(..., description="Company registration number")