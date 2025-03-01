import json
import pickle
class Student:
    def __init__(self, name, age, country):
        self.name=name
        self.age=age
        self.country=country

    def __str__(self):
        return f"Student sa vola {self.name} z krajiny {self.country} a ma {self.age} rokov"

patrik=Student("Patrik", 30, "Slovakia")

file_name = "patrik.json"

# Write the object to a file in JSON format
with open(file_name, "w") as file:
    json.dump(patrik.__dict__, file)

print('_____')
with open(file_name, "r") as file:
    student_data = json.load(file)

patrik_loaded = Student(student_data.get("name"), student_data.get("age"), student_data.get("country"))
print(patrik_loaded)

print('_______')

#zadanie task1:
list_input=[20,30,40,50]
with open('file_to_save.txt', "wb") as file:
    pickle.dump(list_input, file)

with open('file_to_save.txt', "rb") as file:
    read_list=pickle.load(file)

print(list_input)
print(read_list)




#ulozit patrik do suboru
