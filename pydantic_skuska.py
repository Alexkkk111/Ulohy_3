from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
    email:str

patrik=Student(name="Patrik", age=20, email="patrik@dendis.sk")
print(patrik)