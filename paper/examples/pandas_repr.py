import pandas as pd
def _pandas_df_repr(df: pd.DataFrame)->str:
    '''
    Sadly, the 'repr' method for Pandas DataFrames does
    not work the same as 'repr' for built-in types.  
    Specifically, while 'repr' on built-in types 
    (strings, lists, dicts, etc) produces valid Python 
    code that can be instantly used to re-create the 
    original object, this is not true of Pandas 
    DataFrames, which are instead pretty printed as a 
    table. The best alternative for our needs 
    (for non-empty DataFrames) is found in StackOverflow 
    user Silveri's answer at
    https://stackoverflow.com/questions/67845199.
    The code overwrites the native Pandas DataFrame 
    __repr__  method directly, indirectly affecting 
    the repr() method as well.  

    Note: For most use cases overwriting a class's 
    method like this is considered bad practice.
    '''
    return f"DataFrame.from_dict({df.to_dict()})"

pd.DataFrame.__repr__ = _pandas_df_repr