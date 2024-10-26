import pandas as pd

def process_csv(file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Check if 'amount' column exists
    if 'amount' not in df.columns:
        raise ValueError("The CSV file must contain an 'amount' column.")
    
    # Example calculation: Sum of the 'amount' column
    total_amount = df['amount'].sum()

    # Convert the result to a standard Python int or float
    if isinstance(total_amount, pd.Series):
        total_amount = total_amount.values[0]  # Get the first element if it's a Series
    total_amount = int(total_amount)  # Ensure it’s a standard int

    return total_amount
