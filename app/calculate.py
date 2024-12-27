import pandas as pd


def process_csv(file):
    try:
        df = pd.read_csv(file)
        df.columns = ["A", "O", "B"]
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
        return result
    except pd.errors.EmptyDataError:
        raise ValueError("Empty CSV file")
    except Exception as e:
        raise ValueError(f"Error processing CSV file: {e}")
