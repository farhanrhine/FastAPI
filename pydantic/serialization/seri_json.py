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

# get in dict format 
temp = patient1.model_dump_json()

print(temp)
print(type(temp))

