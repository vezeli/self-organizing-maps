def normalize(df):
    """Normalize complete dataframe."""
    df_normalized = (df-df.min())/(df.max()-df.min())
    return df_normalized
