"""
dictionary of dictionaries:
    keys = id
    value = patient dictionary


dictionary represents a patient entry:
{"name": str, "id": int, "blood_type": str, "test_results": [list of tuples]}

{ 101: {"name": "Ann Ables", "id": 101, "blood_type": "O+,
           "test_results": [('HDL', 100), ('LDL', 200)]},
  102: {"name": "Bob Ables", "id": 102, "blood_type": "A+,
           "test_results", []},
  }

"""
from flask import Flask, request, jsonify

app = Flask(__name__)

db = {}


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    """
    POST route to receive a new patient

    This "/new_patient" POST route allows for a new patient to be added to the
    database on the server.  It should receive the following dictionary as a
    JSON string:
        {
            "name": <string containing the name of the patient>,
            "id": <integer that is the patient id number>,
            "blood_type": <string that contains the patient blood type>
        }
    The function then sends this dictionary to a driver function to implement
    the route and receives back an answer and status code to return to the
    requestor.

    Returns:
        string: the result of the route
        int: status code of the request
    """
    # Get the data from the request
    in_dict = request.get_json()
    # Call other functions to do the work
    answer, status = new_patient_driver(in_dict)
    # Return the results
    return answer, status


def new_patient_driver(in_dict):
    """
    Implements the /new_patient POST route

    This function implements the /new_patient POST route.  It receives the
    input data to the POST route as described in the function above.  It then
    calls a generic verification function and sends it the input data as well
    as tuples of expected keys and expected types.  If the verification is not
    successful, a message and 400 status code are returned to the driver
    function.  If the verification is successful, a function is called to
    add the patient to the database and a 200 status code is then returned.

    Args:
        in_dict (dict/any): the input data received by the POST request, which
                             should be a dictionary, but could be any data type

    Returns:
        string: the result of the verification if verification fails, otherwise
                a message indicating successful patient addition
        int: status code of the request: 400 if verification fails, 200 if
             patient successfully added
    """
    expected_keys = ("name", "id", "blood_type")
    expected_types = (str, int, str)
    result = generic_post_route_input_verification(in_dict,
                                                   expected_keys,
                                                   expected_types)
    if result is not True:
        return result, 400
    add_patient_to_database(in_dict)
    return "Patient Added", 200


def generic_post_route_input_verification(in_dict, expected_keys,
                                          expected_types):
    """
    Generic function for validating an input dictionary

    This function receives the input data to a POST route and a list/tuple of
    expected keys and expected value types.  This function verifies that the
    input data is a dictionary, that it contains the keys founds in the
    expected keys, and that the values for the keys are of the expected type.
    If all verifications pass, a boolean value of True is returned.  If any
    verification fails, a string message explaining the failure is returned.
    Note that the list of expected value types should be in the same order as
    the expected keys.

    Args:
        in_dict (dict/any): the input sent to the POST request.  Ideally, it
                             is a dictionary, but could be any type
        expected_keys (list/tuple): a list or tuple of what keys need to be in
                                    the input dictionary
        expected_types (list/tuple): a list or tuple of expected value types,
                                     in the same order as the expected keys

    Returns:
        bool or string:  a boolean value of True if all validations pass, a
                         string with a message if a validation fails.
    """
    if type(in_dict) is not dict:
        return "Data sent with post request must be a dictionary."
    for key in expected_keys:
        if key not in in_dict.keys():
            return "{} key is not found in the input".format(key)
    for ex_type, ex_key in zip(expected_types, expected_keys):
        if type(in_dict[ex_key]) is not ex_type:
            return "{} key should be of type {}".format(ex_key, ex_type)
    return True


def add_patient_to_database(in_dict):
    """
    Adds a new patient record to the database

    This function receives a dictionary containing patient information and
    adds the patient information to the database.  The input dictionary is
    should have the keys 'name', 'id', and 'blood_type'.  These three values
    are added to the patient record as well as a blank list to hold future
    test results.  The patient record is a dictionary, and this dictionary is
    added to the database ('db') as a dictionary value with the key for the
    entry being the patient id number.

    Args:
        in_dict (dict): patient information

    Returns:
        None

    """
    new_patient = {"name": in_dict["name"],
                   "id": in_dict["id"],
                   "blood_type": in_dict["blood_type"],
                   "test_results": []}
    db[in_dict["id"]] = new_patient
    return


@app.route("/add_test", methods=["POST"])
def post_add_test():
    """
    POST route for adding a test result to an existing patient

    This "/add_test" POST route accepts information on a test result for a
    patient and adds that result to the patient's record in the database.  This
    POST request should receive a JSON string containing a dictionary as
    follows:

        {
            "id": <int of patient id>,
            "test_name": <string containing the name of the test>,
            "test_result": <int of test result>
        }
    This input is sent to a driver function to implement the route and receive
    back a message and status code which are then returned to the requestor.

    Returns:
        string: the result of the route
        int: status code of the request
    """
    in_data = request.get_json()
    answer, status = add_test_driver(in_data)
    return answer, status


def add_test_driver(in_data):
    """
    Implements the /add_test POST route

    This function implements the /add_test POST route.  It receives the
    input data to the POST route as described in the function above.  It then
    calls a generic verification function and sends it the input data as well
    as tuples of expected keys and expected types.  If the verification is not
    successful, a message and 400 status code are returned to the driver
    function.  Next, a function is called to verify that the patient id
    received exists in the database.  If not, a message and 400 status code
    are returned to the driver function.  If verification is successful, a
    function is called to add the result to the patient and a 200 status code
    is then returned.

    Args:
        in_data (dict/any): the input data received by the POST request, which
                             should be a dictionary, but could be any data type

    Returns:
        string: the result of the verification if verification fails, otherwise
                a message indicating successful patient addition
        int: status code of the request: 400 if verification fails, 200 if
             test result successfully added
    """
    expected_keys = ("id", "test_name", "test_result")
    expected_types = (int, str, int)
    result = generic_post_route_input_verification(in_data,
                                                   expected_keys,
                                                   expected_types)
    if result is not True:
        return result, 400
    exists = verify_patient_in_db(in_data["id"])
    if exists is False:
        return ("Patient id {} does not exist in database"
                .format(in_data["id"])), 400
    result, status_code = add_test_to_patient(in_data)
    return result, status_code


def verify_patient_in_db(patient_id):
    """
    Verifies that the given patient id exists in the datbase

    This function checks that the given patient id is a key in the database
    variable, indicating that the patient does exist in the database.

    Args:
        patient_id (int): the patient id to verify is in the database

    Returns:
        bool: True if the patient exists in the datbase, False otherwise

    """
    return patient_id in db.keys()


def add_test_to_patient(in_data):
    """
    Add test results to a specific patient record

    This function receives a dictionary as input.  This dictionary will contain
    the "id" key with a value containing the id of the patient for which to add
    the test, the "test_name" key with a string value with the name of the
    test, and the "test_result" key with an integer value of the test result.
    The test name and test results are put into a tuple that is then appended
    to the test results list of the patient entry.  The patient entry is found
    using the patient id as a key in the database.  A message and status code
    of 200 are returned.

    Args:
        in_data (dict): test result for a patient

    Returns:
        string, int:  A success message and status code

    """
    patient = db[in_data["id"]]
    patient["test_results"].append((in_data["test_name"],
                                    in_data["test_result"]))
    return "Test successfully added", 200


@app.route("/get_full_db", methods=["GET"])
def get_full_db():
    """
    Returns the entire database

    This route was added as a diagnostic route that returns the entire database
    so that how the database is being transformed can be seen by a client.

    Returns:
        dict: the complete contents of the database

    """
    return jsonify(db)


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_patient_results(patient_id):
    """
    Returns the available test results for a specific patient

    This "/get_results/<patient_id>" GET route has a variable URL in which the
    id of the patient for whom the tests are needed is included in the URL.
    That portion of the URL is sent to a driver function to implement the
    route.  It then returns the result and status code to the requestor.

    Args:
        patient_id (string): the patient id found in the variable URL

    Returns:
        string, int:  a string containing JSON encoded data and an integer
                      containing the status code

    """
    results, status_code = get_patient_results_driver(patient_id)
    return results, status_code


def get_patient_results_driver(patient_id):
    """
    Returns the available test results for a specific patient

    This function implements the GET route `/get_results/<patient_id>`.
    It receives the portion of the variable URL which contains the id of
    the patient for whom the tests are needed.  That portion of the URL is
    sent to a validation function which will return the integer of the patient
    number and a status code of 200 if the patient exists in the database or
    will return an error message and a 400 status code if there is a problem
    with the given patient id.

    Args:
        patient_id (string): the given patient id

    Returns:
        list or string: a list of test results or a string with an error
                        message
        int: status code indicating success or failure of request

    """
    results, status_code = validate_patient_id_existing(patient_id)
    if status_code == 200:
        answer = db[results]["test_results"]
    else:
        answer = results
    return answer, status_code


def validate_patient_id_existing(patient_id):
    """
    Validate that the patient_id sent is an integer and exists in the database

    This function receives a string that represents the variable URL portion of
    the /get_results/<patient_id> GET request.  This function attemps to
    convert that string into an integer.  If it is unsuccessful, an error
    message is returned with a status code of 404.  If it can be converted to
    an integer, a check is made whether that integer exists in the database.
    If not, a different error message is returned with a status code of 404.
    Otherwise, patient id as an integer is returned with a 200 status code.

    Args:
        patient_id (string): a string to be tested whether it contains an
                             appropriate patient id that exists in the database

    Returns:
        string or int: a string with an error message if the given patient_id
                       is not a proper integer or does not exist in the
                       database, or an integer if it is a valid patient_id
                       found in the database
        int: status code
    """
    try:
        int_id = int(patient_id)
    except ValueError:
        return ("'patient_id' in URL '/get_results/<patient_id>' must be an "
                "integer."), 400
    if verify_patient_in_db(int_id) is False:
        return ("Patient id {} does not exist in database".format(int_id)), 400
    return int_id, 200


if __name__ == "__main__":
    app.run()
