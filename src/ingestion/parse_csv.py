import pandas as pd

def read_csv(file_path):
    """Read a CSV file and return its contents as a formatted string."""
    try:
        df = pd.read_csv(file_path)
        return df.to_string()
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return ""