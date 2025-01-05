# Python Compute API

This project is a simple web application built with Flask that implements an HTTP API for performing calculations based on CSV file input. The application accepts a CSV file containing expressions and returns the computed result.

## Features

- **API Endpoint**: A single endpoint `/api/compute` that accepts CSV files for processing.
- **Authorization**: Implements JWT-based authorization.
- **Input Format**: The application accepts CSV files with three columns: A (left operand), O (operator), and B (right operand).
- **Database**: Uses SQLite for tracking requests and storing results.
- **Error Handling**: Implements error handling to manage potential issues such as missing files or invalid formats.
- **Unit Testing**: Includes tests to verify the functionality of the API and calculation logic.

## Configuration (`config.py`)

The `config.py` file includes settings for:
- Database configuration
- Logging settings
- Other application-specific configurations

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BDAVIDOV91/python-compute-api.git
   cd python-compute-api

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv  # for Linux users
   source venv/bin/activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Create an .env file: Create a .env file in the root directory with the following content:**.
   ```bash
   FLASK_ENV=development
   SECRET_KEY=bgts
   DATABASE_URL=sqlite:///instance/app.db
   LOG_LEVEL=INFO
   UPLOAD_FOLDER=uploads

5. **Run the application**:
   ```bash
   python run.py
   The application will be available at http://127.0.0.1:5000.
 
6. **Running the Tests**:
   1.Activate the virtual environment:
   2.Run the tests using pytest:

   ```bash
   source venv/bin/activate
   pytest tests/

7. **API Endpoint**:
   -Method: POST
   -Authorization: JWT
   -Description: Accepts a CSV file, processes it, and stores the result in the database.
   -Request:
      Header: Authorization: Bearer <token>
      Body: Form-data with a file field named file.
   -Response:
      Success: 200 OK with a JSON body containing the result.
      Error: 400 Bad Request or 500 Internal Server Error with a JSON body containing the error message.

8. **Using SQLite Browser**:
- To view and manage the SQLite database, you can use SQLite Browser. 
- Make sure to install it on your Linux environment and open the database file to track requests and results.

9. **Additional Changes**:
- Updated test_data.py: Modified the script to use test_calculations.csv and save the calculated result.
- Updated __init__.py: Added logic to read and process the test_calculations.csv file and passed the calculated result to the template.
- Updated admin.html: Removed unnecessary lines and ensured the template displays only the relevant information.