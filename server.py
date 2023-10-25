from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "Server on", 200


@app.route("/info", methods=["GET"])
def info():
    a = "This website is authorized by Lucas Ramirez"
    a += "<br>Copyright 2023"


@app.route("/add/<a>/<b>")
def add_number(a, b):
    c = int(a) + int(b)
    return jsonify(c)


@app.route("/hdl_check", methods=["POST"])
def check_hdl_from_internet():
    from blood_calculator import HDL_analysis
    in_data = request.get_json()
    hdl_value = in_data["test_value"]
    answer = HDL_analysis(hdl_value)
    return jsonify(3)

if __name__ == "__main__":
    app.run()