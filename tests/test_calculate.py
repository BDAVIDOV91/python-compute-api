from io import StringIO

import pytest

from app.calculate import process_csv


def test_process_csv_valid():
    data = """A,O,B
1,+,2
3,*,4
5,-,6
8,/,4
"""
    csv_file = StringIO(data)
    result = process_csv(csv_file)
    assert result == 16.0  # Update based on your expected calculation


def test_process_csv_no_amount_column():
    data = """value
100
200
"""
    csv_file = StringIO(data)
    with pytest.raises(
        ValueError, match="The CSV file must contain an 'amount' column."
    ):
        process_csv(csv_file)


def test_process_csv_invalid_operator():
    data = """A,O,B
1,%,2
3,*,4
"""
    csv_file = StringIO(data)
    with pytest.raises(ValueError, match="Invalid operator: %"):
        process_csv(csv_file)


def test_process_csv_empty_file():
    data = ""
    csv_file = StringIO(data)
    with pytest.raises(
        ValueError, match="The CSV file must contain an 'amount' column."
    ):
        process_csv(csv_file)
