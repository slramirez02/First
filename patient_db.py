"""
    Name, mrn, age, tests
    
    ex: ["Ann Ables", 101 35, []]
"""

db = []
def create_db_entry(patient_name, mrn, age):
   new_patient = [patient_name, mrn, age, []]
   return new_patient

def main():
    db.append(create_db_entry("Ann Ables", 101, 35))
    dp.append(create_db_entry("Bob Boyles", 102, 64))
    dp.append(create_db_entry("Chris Chou", 103, 23))
    print(db)
    
if __name__ == "__main__":
    main()

    