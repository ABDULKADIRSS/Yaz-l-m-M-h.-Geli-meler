from flask import Flask

app = Flask(name)

if name == "main":
    app.run(port=44)
