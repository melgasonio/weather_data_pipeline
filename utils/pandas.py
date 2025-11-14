import pandas as pd
import numpy as np

# Convert an array of dictionaries to a dataframe
def convert_to_df(arr):
    return pd.DataFrame(arr)

# Remove a set of columns from a dataframe
def delete_col(df, columns_to_drop):
    return df.drop(columns=columns_to_drop)

# Add a column with a content to a dataframe
def add_col(df, col, content):
    try:
        df[col] = content
        return df
    except ValueError:
        raise ValueError(f"Content length mismatch on column {col}")