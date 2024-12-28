import pandas as pd


def process_csv(file):
    try:
        df = pd.read_csv(file)
        if df.empty:
            raise ValueError("The CSV file is empty.")
        if not all(col in df.columns for col in ["A", "O", "B"]):
            raise ValueError("The CSV file must contain 'A', 'O', and 'B' columns.")

        result = 0
        for index, row in df.iterrows():
            if row["O"] == "+":
                result += row["A"] + row["B"]
            elif row["O"] == "-":
                result += row["A"] - row["B"]
            elif row["O"] == "*":
                result += row["A"] * row["B"]
            elif row["O"] == "/":
                result += row["A"] / row["B"]
            else:
                raise ValueError(f"Invalid operator: {row['O']}")
        return result
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.")
    except Exception as e:
        raise ValueError(f"Error processing CSV file: {e}")
