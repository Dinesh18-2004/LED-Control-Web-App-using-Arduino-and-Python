import serial
import time
from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Connect to Arduino (Change COM port if needed)
arduino = serial.Serial('COM10', 9600, timeout=1)
time.sleep(2)  # Allow time for Arduino to initialize

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-size: cover;
            background-position: center;
            color: white;
            padding: 20px;
            transition: background 0.5s ease-in-out;
        }

        h1 {
            margin-bottom: 20px;
        }

        .switch-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }

        .switch {
            position: relative;
            display: inline-block;
            width: 80px;
            height: 40px;
        }

        .switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }

        .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #d32f2f; /* Default Red (OFF) */
            transition: 0.4s;
            border-radius: 40px;
        }

        .slider:before {
            position: absolute;
            content: "";
            height: 32px;
            width: 32px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            transition: 0.4s;
            border-radius: 50%;
        }

        input:checked + .slider {
            background-color: #28a745; /* Green when ON */
        }

        input:checked + .slider:before {
            transform: translateX(40px);
        }

        .status-text {
            font-size: 20px;
            font-weight: bold;
        }

        /* Background Option Buttons */
        .bg-buttons {
            margin-top: 20px;
        }

        .bg-buttons button {
            padding: 10px 15px;
            font-size: 16px;
            margin: 5px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #007BFF;
            color: white;
        }

        .bg-buttons button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body id="body">

    <h1>Control 5 LEDs</h1>
    
    <div class="switch-container">
        {% for i in range(1, 6) %}
            <label class="switch">
                <input type="checkbox" id="led{{i}}" onchange="toggleLED({{i}}, this)">
                <span class="slider"></span>
            </label>
            <p class="status-text">LED {{i}}</p>
        {% endfor %}
    </div>

    <!-- Background Selection Buttons -->
    <div class="bg-buttons">
        <button onclick="changeBackground(1)">Online Image</button>
        <button onclick="changeBackground(2)">Local Image</button>
        <button onclick="changeBackground(3)">Gradient</button>
    </div>

    <script>
        function toggleLED(ledNumber, element) {
            let command = element.checked ? "LED" + ledNumber + "_ON" : "LED" + ledNumber + "_OFF";
            fetch('/control/' + command);
        }

        function changeBackground(option) {
            let body = document.getElementById("body");

            if (option === 1) {
                body.style.backgroundImage = "url('https://source.unsplash.com/1600x900/?technology')";
            } else if (option === 2) {
                body.style.backgroundImage = "url('{{ url_for('static', filename='bg.jpg') }}')";
            } else if (option === 3) {
                body.style.background = "linear-gradient(to right, #ff7e5f, #feb47b)";
            }
        }
    </script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/control/<command>')
def control(command):
    arduino.write((command + "\n").encode())  # Send command to Arduino
    return "", 204  # No content response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
