from flask import Flask, request, jsonify

app = Flask(name)

@app.route("/add", methods=["GET"])
def add_numbers():
    num1 = int(request.args.get("num1", 0))
    num2 = int(request.args.get("num2", 0))
    result = num1 + num2
    return jsonify({"result": result})

if name == "main":
    app.run(port=44)
