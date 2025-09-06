from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    # Flask's jsonify() automatically sets Content-Type to application/json
    return jsonify(message="Hello, JSON world!")

@app.route("/echo", methods=["POST"])
def echo():
    if request.is_json:  # Checks Content-Type: application/json
        data = request.get_json()
        return jsonify(received=data)
    else:
        return jsonify(error="Expected application/json"), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
