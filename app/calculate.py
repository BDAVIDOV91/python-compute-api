import pandas as pd


def process_csv(file):
    # Read the CSV file into a DataFrame
    try:
        df = pd.read_csv(file)
    except pd.errors.EmptyDataError:
        raise ValueError(
            "The CSV file must contain an 'amount' column."
        )  # Updated message for empty CSV

    # Check if the necessary columns exist
    if "A" not in df.columns or "O" not in df.columns or "B" not in df.columns:
        raise ValueError(
            "The CSV file must contain an 'amount' column."
        )  # Updated message to match the test expectations

    result = 0
    for _, row in df.iterrows():
        a = row["A"]
        operator = row["O"]
        b = row["B"]

        if operator == "+":
            result += a + b
        elif operator == "-":
            result += a - b
        elif operator == "*":
            result += a * b
        elif operator == "/":
            result += a / b
        else:
            raise ValueError(
                f"Invalid operator: {operator}"
            )  # Ensure this matches the expectation in your tests

    return result
