from flask import Flask, request, jsonify

app = Flask(name)

@app.route("/add", methods=["GET"])
def add_numbers():
    num1 = int(request.args.get("num1", 0))
    num2 = int(request.args.get("num2", 0))
    result = num1 + num2
    return jsonify({"result": result})

@app.route("/multiply", methods=["POST"])
def multiply_numbers():
    data = request.get_json()
    num1 = data.get("num1", 1)
    num2 = data.get("num2", 1)
    result = num1 * num2
    return jsonify({"result": result})

if name == "main":
    app.run(port=44)
