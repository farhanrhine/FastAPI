from pydantic import BaseModel
from typing import List, Dict, Optional


# Step 1: Define the model
class Patient(BaseModel):
    name : str | None = None # type validation
    age : int | None = None
    weight : float | None = None
    married : bool | None = None
    allergies : Optional[List[str]] = None # list of strings
    contact_details : Optional[Dict[str, str]] = None # dictionary with string keys and values



# Step 2: Instantiate (Validation runs here)
patient_info = {"age" : 22, "weight": 70.5, "married": False,
                 "contact_details": {"email": "farhan@example.com", "phone": "123-456-7890"}} # simple dict

patient1 = Patient(**patient_info)

# Step 3: Use the validated object
def insert_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

insert_patient_data(patient1)     

