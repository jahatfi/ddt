import pandas as pd
def _pandas_df_repr(df: pd.DataFrame)->str:
    '''
    The 'repr' method for Pandas DataFrames does
    not work the same as 'repr' for built-in types.  
    StackOverflow user Silveri answer at
    https://stackoverflow.com/questions/67845199.
    provides a solution. The code overwrites the 
    native Pandas DataFrame __repr__  method directly,
    indirectly affecting the repr() method as well.  

    Note: For most use cases overwriting a class's 
    method like this is considered bad practice.
    '''
    return f"DataFrame.from_dict({df.to_dict()})"

pd.DataFrame.__repr__ = _pandas_df_repr