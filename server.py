from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "Server on"

if __name__ == "__main__":
    app.run()