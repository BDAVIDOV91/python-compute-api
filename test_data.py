from app import create_app
from app.db import save_request, save_result
from app.calculate import process_csv

app = create_app()

with app.app_context():
    # Add test request
    request_id = save_request(user="user1", filename="data/test_calculations.csv")

    # Process the CSV file to calculate the result
    calculation_result = process_csv("data/test_calculations.csv")

    # Add test result
    save_result(request_id=request_id, result=calculation_result)

    print("Test data added successfully.")
