import pandas as pd
import numpy as np
from .functions import check_type, check_column, log

def number_range(data, targetColumn, min = np.nan, max = np.nan, file = 'Error_Log'):
    """
    Number validation\n
    data: Data source for validation\n
    targetColumn: Column name that requires for validation\n
    min: Minimum value of data. If none, leave it blank or set to np.nan\n
    max: Maximum value of data. If none, leave it blank or set to np.nan\n
    file: Invalid output text file name. E.g. ".\\Output\\Error_Log" store log with Error_Log name in Output folder
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
        raise Exception('Invalid number detected.')
