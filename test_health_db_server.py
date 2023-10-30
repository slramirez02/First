import pytest
good_patient = {"name": "Ann", "id": 102, "blood_type": "O-"}


def test_add_patient_to_database():
    from health_db_server import add_patient_to_database
    out_dict = {"name": "Ann", "id": 102, "blood_type": "O-"}
    add_patient_to_database(out_dict)
    from health_db_server import db
    answer = list(db.keys())
    patient = db[102]
    db.clear()
    assert 102 in answer
    assert patient["name"] == "Ann"
    assert len(patient["test_results"]) == 0


@pytest.mark.parametrize("in_dict, expected", [
    ({"name": "Lucas", "id": 104, "blood_type": "O-"}, {"Patient Added", 200}),
    ({}, ("name key is not found in the input", 400)),
    ("string", ("Data sent with post request must be a dictionary.", 200))
])
def test_new_patient_driver(in_dict, expected):
    from health_db_server import new_patient_driver
    answer, status_code = new_patient_driver(in_dict)
    assert answer, status_code == expected


def test_add_test_to_patient():
    from health_db_server import add_test_to_patient, add_patient_to_database
    from health_db_server import db
    add_patient_to_database(good_patient)
    out_data = {"id": 102, "test_name": "HDL", "test_result": 130}
    answer = add_test_to_patient(out_data)
    db_answer = db[102]
    db.clear()
    assert answer == ("Test successfully added", 200)
    assert db_answer["test_results"] == [("HDL", 130)]
