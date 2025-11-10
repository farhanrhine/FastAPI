from pydantic import BaseModel
from typing import List, Dict, Optional, Annotated  


class Address(BaseModel):
    city : str | None = None
    state : str | None = None
    pin_code : int | None = None



class Patient(BaseModel):

    name : str | None = None
    gender : str | None = None
    age : int | None = None
    address : Address # Nested Model

address_dict = {"city": "Chandigarh",
                "state": "Punjab",
                "pin_code": 160017}

address1 = Address(**address_dict)

patient_info = {"name": "farhan", "gender": "male", "age" : 22, "address": address1} # simple dict

patient1 = Patient(**patient_info)

# can we get any specific fields from nested model
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin_code)
