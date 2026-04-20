#design data validation for full name
from pydantic import BaseModel, Field
class FullName(BaseModel):
    first_name: str = Field(..., pattern="^[A-Za-z]+$", description="First name of the person")
    last_name: str = Field(..., pattern="^[A-Za-z]+$", description="Last name of the person")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"