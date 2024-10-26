import pandas as pd


def process_csv(file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Check if the necessary columns exist
    if "A" not in df.columns or "O" not in df.columns or "B" not in df.columns:
        raise ValueError("The CSV file must contain 'A', 'O', and 'B' columns.")

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
            raise ValueError(f"Unsupported operator: {operator}")

    return result
