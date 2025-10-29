# Real-Time Weather Tracker 🌦

A **Flask-based real-time weather web application** that allows users to get current weather information for any city, including temperature, humidity, wind speed, and weather condition.

---

## Features

- Search weather by **city name**
- Displays:
  - **Temperature**
  - **Feels Like Temperature**
  - **Humidity**
  - **Wind Speed**
  - **Weather Condition**
  - **Weather Icon**
- Clean and responsive **HTML/CSS frontend**
- Powered by **OpenWeatherMap API**
- Built with **Python (Flask)**

---

## Screenshots

![Weather App Screenshot](screenshot.png)  

---

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mohammednouman555/real_time_weather_tracker.git](https://github.com/mohammednouman555/real_time_weather_tracker.git)
    cd real_time_weather_tracker
    ```

2.  **Create and activate a virtual environment** (recommended):

    * Create the environment:
        ```bash
        python -m venv .venv
        ```
    * Activate the environment:
        * On Windows:
            ```bash
            .venv\Scripts\activate
            ```
        * On Linux/Mac:
            ```bash
            source .venv/bin/activate
            ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    * (If `requirements.txt` is missing, install manually):
        ```bash
        pip install flask requests
        ```

4.  **Add your OpenWeatherMap API Key:**
    * Open the `app.py` file.
    * Find the line `API_KEY = "YOUR_API_KEY_HERE"` and replace `"YOUR_API_KEY_HERE"` with your actual API key.

5.  **Run the Flask server:**
    ```bash
    python app.py
    ```

6.  **Open your browser** and visit:
    `http://127.0.0.1:5000`

---

## Project Structure
real_time_weather_tracker/
│
├── app.py # Flask backend
├── weather_app.py # Optional CLI version ├── templates/
    │
    └── weather.html # HTML frontend 
├── static/
    │ 
    └── style.css # Optional CSS
    └── README.md

---

## Technologies Used

* Python 3
* Flask
* OpenWeatherMap API
* HTML / CSS / JavaScript

---

## License

This project is licensed under the **MIT License**.
Feel free to use, modify, and share!

---

## Author

**Mohammed Nouman**
* **GitHub:** [@mohammednouman555](https://github.com/mohammednouman555)
* **Email:** mohammednouman555@gmail.com
