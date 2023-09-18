"""
    Name, mrn, age, tests
    
    ex: ["Ann Ables", 101 35, []]
"""

db = []
def create_db_entry(patient_name, mrn, age):
   new_patient = [patient_name, mrn, age, []]
   return new_patient

def printdb():
    rooms = ["A3", "B1", "C2"]
    for i, p in enumerate(db):
        print("Name: {}, MRN: {}, Age: {}, Room: {}".format(p[0], p[1], p[2], rooms[i]))
    for room, p, in zip(rooms, db):
        print("Name: {}, MRN: {}, Age: {}, Room: {}".format(p[0], p[1], p[2], room))

def main():
    db.append(create_db_entry("Ann Ables", 101, 35))
    db.append(create_db_entry("Bob Boyles", 102, 64))
    db.append(create_db_entry("Chris Chou", 103, 23))
    print(db)

def find_patient(mrn):
    answer = []
    for p in db:
        if p[1] == mrn:
            answer = p
    if answer == []:
        print("Patient not found.")
    else:
        print(answer)
    
if __name__ == "__main__":
    main()
    printdb()
    find_patient(102)

    