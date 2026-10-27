from numpy import nan
import pandas as pd

def evaluate_df(df):
    """
    Evaluates a dataframe and 
    returns information on each column
    
    Args:
        df (Pandas.Dataframe): dataframe to evaluate
        
    Returns:
        eval_df(Pandas.Dataframe): a dataframe of each column
        and associated univariate stats organized by numeric or categorical
    """
    rows = []
    columns = [
        "column_name", 
        "is_numeric", 
        "mean", 
        "median", 
        "min", 
        "max", 
        "Q25", 
        "Q75", 
        "std", 
        "num_null", 
        "num_unique", 
        "uniques<5"]

    for col in df.columns:
        col_name = col 
        is_numeric = pd.api.types.is_numeric_dtype(df[col])
        mean= nan 
        median= nan 
        minimum= nan 
        maximum= nan 
        q25= nan 
        q75= nan 
        std= nan 
        num_null= df[col].isna().sum()
        num_unique= nan 
        uniques5= nan

        if is_numeric:
            mean= df[col].mean()
            median= df[col].median()
            minimum= df[col].min()
            maximum= df[col].max()
            q25= df[col].quantile(0.25)
            q75= df[col].quantile(0.75)
            std= df[col].std()
        else:
            num_unique= df[col].nunique() 
            uniques5= df[col].unique() if num_unique <= 5 else nan

        row = [
            col_name,
            is_numeric,
            mean,
            median,
            minimum,
            maximum,
            q25,
            q75,
            std,
            num_null,
            num_unique,
            uniques5,
        ]
        rows.append(row)

    eval_df = pd.DataFrame(data=rows, columns=columns)

    return eval_df.sort_values(by="is_numeric")