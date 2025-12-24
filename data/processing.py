import pandas as pd

def to_dataframe(data):
    """Converte lista de dicts em DataFrame pandas."""
    return pd.DataFrame(data) if isinstance(data, list) else pd.DataFrame()

def show_dataframe(df, max_rows=10):
    print(df.head(max_rows))