from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Observability Demo App Running"

@app.route("/slow")
def slow():
    time.sleep(random.randint(1, 3))
    return "Slow response simulated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
