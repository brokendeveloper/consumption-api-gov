import pandas as pd
pd.set_option('display.float_format', '{:,.2f}'.format)

def to_dataframe(data):
    """Converte lista de dicts em DataFrame pandas."""
    return pd.DataFrame(data)

def show_dataframe(df, max_rows=10):
    """Exibe as primeiras linhas do DataFrame."""
    print(df.head(max_rows))