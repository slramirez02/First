"""
    Name, mrn, age, tests
    
    ex: ["Ann Ables", 101 35, []]
"""
from patient_db_class import Patient

db = []
def create_db_entry(firstName, lastName, mrn, age):
   new_patient = Patient()
   new_patient.first_name = firstName
   new_patient.last_name = lastName
   new_patient.mrn = mrn
   new_patient.age = age
   
   return new_patient

def printdb():
    rooms = ["A3", "B1", "C2"]
    for i, p in enumerate(db):
        print("Name: {}, MRN: {}, Age: {}, Room: {}".format(p[0], p[1], p[2], rooms[i]))
    for room, p, in zip(rooms, db):
        print("Name: {}, MRN: {}, Age: {}, Room: {}".format(p[0], p[1], p[2], room))

def main():
    p = create_db_entry("Ann", "Ables", 101, 35)
    print(p.last_name)
    print(p.print())
    return
    db.append(create_db_entry("Bob Boyles", 102, 64))
    db.append(create_db_entry("Chris Chou", 103, 23))
    print(db)

def find_patient(mrn):
    answer = []
    for i, p in enumerate(db):
        if p[1] == mrn:
            answer = p
            ind = i
    if answer == []:
        print("Patient not found.")
        ind = -1 
    else:
        return ind, answer
        
def add_testresult(mrn, test_name, test_result):
    patient_ind = find_patient(mrn)[0]
    db[patient_ind][3].append((test_name, test_result))
    print(db)
    
    
if __name__ == "__main__":
    main()
    exit()
    printdb()
    find_patient(102)
    add_testresult(102, "weight", "125")

    