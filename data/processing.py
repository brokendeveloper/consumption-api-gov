import pandas as pd

def to_dataframe(data):
    """Converte lista de dicts em DataFrame pandas."""
    return pd.DataFrame(data)

def show_dataframe(df, max_rows=10):
    """Exibe as primeiras linhas do DataFrame."""
    print(df.head(max_rows))