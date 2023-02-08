import pandas as pd
from .functions import check_type, check_column, log

def require(data, targetColumn, file = 'Error_Log.txt'):
    """
    Require validation\n
    Raise error when data is empty or null.\n
    Invalid data will store in text file with location and name that declared in 'file'.\n

    Parameters:
    data (pd.DataFrame): Data source for validation.
    targetColumn (list): Column name that requires for validation.
    file (str): Invalid output text file.  

    Raises:
    TypeError: if parameters invalid type
    Exception: if invalid data detected   
    """

    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    
    invalid = False
    logContent = ''

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return null or empty value rows
        df = data[data[column].isnull()]

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that contains null or empty value: {} row(s)\n\n'.format(len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Null or empty value detected. View more in ' + file)
