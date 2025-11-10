'''That’s exactly the core philosophy of Pydantic:
👉 "Define data shape once, validate everywhere automatically.'''
from pydantic import BaseModel


# Step 1: Define the model
class Patient(BaseModel):
    name : str # type validation
    age : int 

# Step 2: Instantiate (Validation runs here)
patient_info = {"name" : "farhan", "age" : 22} # simple dict

patient1 = Patient(**patient_info) # unpacking the dict and storing it in patient1 object

# Step 3: Use the validated object
def insert_patient_data(patient: Patient): # 'patient' = parameter
    print(patient.name)
    print(patient.age)

insert_patient_data(patient1)     # 'patient1' = argument

"""

👉 Parameter = Placeholder (defined in function)
👉 Argument = Actual value (passed to function)

| Term          | Example in Your Code | Description                                          |
| ------------- | -------------------- | ---------------------------------------------------- |
| **Parameter** | `patient`            | Temporary variable inside the function               |
| **Argument**  | `patient1`           | The actual object you pass when calling the function |


"""
