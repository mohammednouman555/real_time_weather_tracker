from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "a7bb13c93491405aeb3d86df4f737eeb"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def home():
    return render_template("weather.html")

@app.route("/get_weather")
def get_weather():
    city = request.args.get("city")
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
