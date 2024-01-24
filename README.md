# Sunspot

## Overview
Sunspot is a simple Flask API designed to record sunlight data on a Raspberry Pi using the Seeedstudio's Grove - Sunlight Sensor. It uses `flask_pymongo`, `Flask-APScheduler`, and `seeed-python-si114x` to record sunlight intensity, UV index, and infrared light levels in programmable timed intervals. My `si114x` chipset records its absolute darkeness limitation at 260 lumins.

## Features
- Periodic data collection with APScheduler.
- Sunlight data includes visibility, UV index, and IR levels.
- Data storage using Flask-PyMongo.
- Configurable intervals for data recording.

## Installation

This application is designed to be configured on a Raspberry Pi running Debian (I'm using the Debian Bookworm kernel).
Hook up Si114x to Raspberry Pi

### Connect the Si114x to the Pi's GPIO, GND, and VCC 3.3V. Here's how I connected it:
- 3.3V Power (VCC): Pin 1
- Ground (GND): Pin 6
- SDA (Serial Data Line): Pin 3
- SCL (Serial Clock Line): Pin 5

### Ensure Your Raspberry Pi has the I2C Interface Enabled
- Run `sudo raspi-config`.
- Navigate to Interfacing Options > I2C and select "Yes" to enable the I2C interface.

### Install I2C Tools
- Install I2C tools to help diagnose communication with the sensor by running `sudo apt-get install i2c-tools`.

### Detect the Sensor
- Use the command `sudo i2cdetect -y 1` to check if the Raspberry Pi detects the sensor. The sensor should appear at `0x60` for Si114x.

### Configuration
- Create a `.env` file in your project directory.
- Add a key named `MONGO_URI` and set its value to your Mongo Cloud DB URI or a local MongoDB URI. This will be used for database connections.

### To Get the Python Portion Working Inside the Working Directory
- Install venv with `python3 -m venv venv`.
- Activate venv with `source venv/bin/activate`.
- Install packages with `pip3 install -r requirements.txt`.
- Run the program with `python3 run.py`.
- I use `systemctl` to run the application in the background.


## Configuration
- Create a .env file with a key of MONGO_URI and value from Mongo Cloud DB or local URI
