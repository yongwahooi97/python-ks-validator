import pandas as pd
from .functions import check_type, check_column, log

def unique(data, targetColumn, file = 'Error_Log.txt'):
    """
    Unique validation\n
    Raise error when data is duplicated.\n
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

        # Return duplicate rows
        df = data[data.duplicated([column], keep=False)]

        # Invalid data
        if not df.empty:
            invalid = True
            dfGroupBy = df.groupby(column)
            logContent += 'Column: ' + column
            logContent += '\nDuplicate value: \n'
            for name, group in dfGroupBy:
                logContent += '- {} ({} rows)\n'.format(name, len(group))
            logContent += '\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Duplicated value detected. View more in ' + file)
