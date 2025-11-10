from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated


# Step 1: Define the model
class Patient(BaseModel):
    name : Annotated[str, Field(min_length=1, max_length=50, description="The name of the patient", examples=["John Doe"])] | None = None
    age : int
    email : EmailStr | None = None
    linkdin_profile : AnyUrl | None = None
    weight : float = Field(..., gt=0, description="Weight must be greater than 0")
    married : bool | None = None
    allergies : Optional[List[str]] = None # list of strings
    contact_details : Optional[Dict[str, str]] = None # dictionary with string keys and values

    # Model validator for cross-field validation
    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and (self.contact_details is None or "emergency" not in self.contact_details):
            raise ValueError("Emergency contact is required for patients over 60.")
        return self


# Step 2: Instantiate (Validation runs here)
patient_info = {"name": "farhan", "age" : 70, "email": "farhan@cuchd.in", "weight": 65.0, "married": False,
                 "linkdin_profile": "https://www.linkedin.com/in/farhanrhine/", "contact_details": {"phone": "123-456-7890", "emergency": "987-654-3210"}} # simple dict

patient1 = Patient(**patient_info)

# Step 3: Use the validated object
def insert_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkdin_profile)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

insert_patient_data(patient1)     

