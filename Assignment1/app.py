from flask import Flask, jsonify

app = Flask(__name__, static_folder="public", static_url_path="../public")

@app.get("/")
def index():
    return "Welcome to my Flask API!"

@app.get("/api/v1/cat")
def get_cat():
    cat_data = {
        "cat_id": "1",
        "name": "Whiskers",
        "birthdate": "2021-05-12",
        "weight": 4.5,
        "owner": "Owner123",
        "image": "http://127.0.0.1:3000/public/cat.jpg"
    }
    return jsonify(cat_data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)


