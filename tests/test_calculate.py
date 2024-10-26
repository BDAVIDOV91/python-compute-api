# tests/test_calculate.py
import pytest
from app.calculate import process_csv
import pandas as pd
from io import StringIO

def test_process_csv_valid():
    data = """amount
    100
    200
    300
    """
    csv_file = StringIO(data)
    result = process_csv(csv_file)
    assert result == 600

def test_process_csv_no_amount_column():
    data = """value
    100
    200
    """
    csv_file = StringIO(data)
    with pytest.raises(ValueError, match="The CSV file must contain an 'amount' column."):
        process_csv(csv_file)
