from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
from typing import List, Dict, Optional, Annotated


# Step 1: Define the model
class Patient(BaseModel):
    name : Annotated[str, Field(min_length=1, max_length=50, description="The name of the patient", examples=["John Doe"])] | None = None
    age : int
    email : EmailStr | None = None
    linkdin_profile : AnyUrl | None = None
    weight : float = Field(..., gt=0, description="Weight must be greater than 0 in kg")
    height : float = Field(..., gt=0, description="Height must be greater than 0 in cm") 
    married : bool | None = None
    allergies : Optional[List[str]] = None # list of strings
    contact_details : Optional[Dict[str, str]] = None # dictionary with string keys and values

# computed field for BMI

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100  # Convert cm to meters
        bmi = round(self.weight / (height_in_meters ** 2), 2)
        return bmi


# Step 2: Instantiate (Validation runs here)
patient_info = {"name": "farhan", "age" : 22, "email": "farhan@cuchd.in", "weight": 65.0, "height": 175.0, "married": False,
                 "linkdin_profile": "https://www.linkedin.com/in/farhanrhine/", "contact_details": {"phone": "123-456-7890"}} # simple dict

patient1 = Patient(**patient_info)

# Step 3: Use the validated object
def insert_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkdin_profile)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI:", patient.bmi)


insert_patient_data(patient1)     

