# LED Control Web App using Arduino and Python

This project allows you to control multiple LEDs connected to an Arduino board via a simple Python-based web interface using Flask.

##  Technologies Used
- Arduino UNO
- Python (Flask)
- HTML + CSS (TailwindCSS optional)
- Serial Communication (pyserial)

##  Features
- Control individual LEDs through ON/OFF buttons
- Turn All ON/OFF functionality
- Web-based interface to interact with hardware
- Real-time serial communication between Python and Arduino

##  How It Works
1. Python Flask server runs locally and serves the web UI.
2. Web UI sends requests (ON/OFF) to the Flask backend.
3. Flask writes commands to the serial port.
4. Arduino reads commands and controls LEDs accordingly.

##  Future Scope
- Add status feedback (LED state) to the UI
- Host the app on a local network or cloud
- Extend to control other devices like motors or buzzers
