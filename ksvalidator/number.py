import pandas as pd
import numpy as np
from .functions import check_type, check_column, log

def number_range(data, targetColumn, min = np.nan, max = np.nan, file = 'Error_Log.txt'):
    """
    Number validation\n
    Raise error when data does not within range.\n
    Invalid data will store in text file with location and name that declared in 'file'.\n

    Parameters:
    data (pd.DataFrame): Data source for validation.
    targetColumn (list): Column name that requires for validation.    
    min (int, float): Minimum value of data. If none, leave it blank or set to np.nan\n
    max (int, float): Maximum value of data. If none, leave it blank or set to np.nan\n
    file (str): Invalid output text file.  

    Raises:
    TypeError: if parameters invalid type
    Exception: if invalid data detected
    """

    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    if not pd.isnull(min):
        check_type((int, float), 'min', min, file)
    if not pd.isnull(max):
        check_type((int, float), 'max', max, file)

    invalid = False
    logContent = ''

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        desc = ''
        # Return rows that not within range / below min / above max
        df = pd.DataFrame()
        if pd.isnull(min) & pd.isnull(max):
            df = pd.DataFrame()
        if pd.isnull(min):
            df = data[~(data[column] <= max)]
            desc = 'less than or equal to {}'.format(max)
        elif pd.isnull(max):
            df = data[~(data[column] >= min)]
            desc = 'greater than or equal to {}'.format(min)
        else:
            df = data[~data[column].between(min, max)]
            desc = 'between {} and {}'.format(min, max)

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that not {}: {} row(s)\n\n'.format(desc, len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Invalid number detected. View more in ' + file)
