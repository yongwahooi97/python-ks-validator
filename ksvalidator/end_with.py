import pandas as pd
from .functions import check_type, check_column, log

def end_with(data, targetColumn, condition, file = 'Error_Log.txt'):
    """
    End with validation
    Raise error when data does not end with 'condition'.\n
    Invalid data will store in text file with location and name that declared in 'file'.\n

    Parameters:
    data (pd.DataFrame): Data source for validation
    targetColumn (list): Column name that requires for validation
    condition (str): End with condition (Support multiple conditions by delimiter (,) E.g. A,B,C)\n
    file (str): Invalid output text file.  
    
    Raises:
    TypeError: if parameters invalid type
    Exception: if invalid data detected
    """

    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    check_type(str, 'condition', condition, file)

    invalid = False
    logContent = ''

    strConditions = condition.split(',')

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return rows that not end with 'condition'
        df = data[~data[column].map(str).str.endswith(tuple(strConditions), na=False)]

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that not end with `{}`: {} row(s)\n\n'.format(condition, len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Invalid end with detected. View more in ' + file)
