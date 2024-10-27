# Python Compute API

This project is a simple web application built with Flask that implements an HTTP API for performing calculations based on CSV file input. The application accepts a CSV file containing expressions and returns the computed result.

## Features

- **API Endpoint**: A single endpoint `/api/compute` that accepts CSV files for processing.
- **Authorization**: Implements simple static authorization via a predefined passphrase.
- **Input Format**: The application accepts CSV files with three columns: A (left operand), O (operator), and B (right operand).
- **Database**: Uses SQLite for tracking requests and storing results.
- **Error Handling**: Implements error handling to manage potential issues such as missing files or invalid formats.
- **Unit Testing**: Includes tests to verify the functionality of the API and calculation logic.

## Configuration (`config.py`)
The `config.py` file is currently a work in progress. It will include settings for:
- Database configuration
- Logging settings
- Other application-specific configurations

Plans for completion include:
- Defining the database URI for SQLite.
- Configuring logging levels and formats for better tracking of application behavior.
- Adding any additional settings that may be required as the application evolves.


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BDAVIDOV91/python-compute-api.git
   cd <location-repository-name>

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv  # for Linux users
   source venv/bin/activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Set up the database: Make sure to initialize the SQLite database if it hasn't been done already**.

5. **Run the application**:
   ```bash
   export FLASK_APP=app
   export FLASK_ENV=development
   flask run         # In my case i use "flask run --port=5001" because port = 5000 was busy
 
6. **Testing the API**:
   ```bash
   curl -X POST http://127.0.0.1:5001/api/compute -H "Authorization: mypass123" -F "file=@data/test_calculations.csv" # Check ports before runing 

7. **Using SQLite Browser**:
- To view and manage the SQLite database, you can use SQLite Browser. 
- Make sure to install it on your Linux environment and open the database file to track requests and results.