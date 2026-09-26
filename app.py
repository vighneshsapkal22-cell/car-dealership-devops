import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

cars = [
    {
        "id": 1,
        "brand": "Toyota",
        "model": "Fortuner",
        "year": 2024,
        "price": 4200000,
        "fuel": "Diesel",
        "transmission": "Automatic"
    },
    {
        "id": 2,
        "brand": "Hyundai",
        "model": "Creta",
        "year": 2025,
        "price": 1850000,
        "fuel": "Petrol",
        "transmission": "Automatic"
    },
    {
        "id": 3,
        "brand": "Tata",
        "model": "Nexon",
        "year": 2024,
        "price": 1250000,
        "fuel": "Petrol",
        "transmission": "Manual"
    },
    {
        "id": 4,
        "brand": "Mahindra",
        "model": "XUV700",
        "year": 2025,
        "price": 2400000,
        "fuel": "Diesel",
        "transmission": "Automatic"
    },
    {
        "id": 5,
        "brand": "Honda",
        "model": "City",
        "year": 2023,
        "price": 1450000,
        "fuel": "Petrol",
        "transmission": "Manual"
    }
]


@app.route("/")
def home():
    return render_template("index.html", cars=cars)


@app.route("/api/cars")
def get_cars():
    return jsonify(cars)


@app.route("/api/cars/<int:car_id>")
def get_car(car_id):
    car = next((car for car in cars if car["id"] == car_id), None)

    if car is None:
        return jsonify({"error": "Car not found"}), 404

    return jsonify(car)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "Car Dealership Management System"
    })


@app.route("/search")
def search():
    query = request.args.get("q", "").lower()

    results = [
        car for car in cars
        if query in car["brand"].lower()
        or query in car["model"].lower()
    ]

    return render_template("index.html", cars=results, search_query=query)


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)