def export_to_csv(df, filename):
    """Exporta DataFrame para CSV."""
    df.to_csv(filename, index=False)

def export_to_excel(df, filename):
    """Exporta DataFrame para Excel."""
    df.to_excel(filename, index=False)