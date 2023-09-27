"""
    Name, mrn, age, tests
    
    ex: ["Ann Ables", 101 35, []]
"""

db = {}
def create_db_entry(firstName, lastName, mrn, age):
   new_patient = {
   "First Name" : firstName, 
   "Last Name" : lastName, 
   "MRN" : mrn,
   "Age" : age,
   "Tests": []}
   return new_patient

def printdb():
    for patient in db.values():
        print("Name: {}, MRN: {}, Age: {}"
            .format(get_fullname(patient),
                    patient["MRN"],
                    patient["Age"]))
    '''
    rooms = ["A3", "B1", "C2"]
    for i, p in enumerate(db):
        print("Name: {}, MRN: {}, Age: {}, Room: {}".format(p[0], p[1], p[2], rooms[i]))
    for room, p, in zip(rooms, db):
        print("Name: {}, MRN: {}, Age: {}, Room: {}".format(p[0], p[1], p[2], room))
    '''

def get_fullname(patient):
    return "{} {}".format(patient["First Name"],
                          patient["Last Name"])
def main():
    db[101] = create_db_entry("Ann", "Ables", 101, 35)
    db[102] = create_db_entry("Bob", "Boyles", 102, 64)
    db[103] = create_db_entry("Chris", "Chou", 103, 23)
    #print(db)

def find_patient(mrn):
    answer = False
    for patient in db.values():
        if patient["MRN"] == mrn:
            answer = patient
            break
    print(answer)
    return answer
    '''
    for i, p in enumerate(db):
        if p[1] == mrn:
            answer = p
            ind = i
    if answer == []:
        print("Patient not found.")
        ind = -1 
    else:
        return ind, answer
    '''
def add_test_to_patient(mrn, test_name, test_result):
    patient = find_patient(mrn)
    patient["Tests"].append((test_name, test_result))
    
def minor_or_adult(patient):
    age = patient["Age"]
    answer = ""
    if age >= 18:
        answer = "Adult"
    else:
        answer = "Minor"
    return answer
            

    
    
if __name__ == "__main__":
    main()
    add_test_to_patient(102, "weight", "125")
    find_patient(102)
    printdb()

    