import pandas as pd
from .functions import check_type, check_column, log

def regex(data, targetColumn, regex, file = 'Error_Log.txt'):
    """
    Regular expression validation
    Raise error when data does not match 'regex'.\n
    Invalid data will store in text file with location and name that declared in 'file'.\n

    Parameters:
    data (pd.DataFrame): Data source for validation.
    targetColumn (list): Column name that requires for validation.
    regex (str): Regular expression pattern. (https://regex101.com/)
    file (str): Invalid output text file.  

    Raises:
    TypeError: if parameters invalid type
    Exception: if invalid data detected   
    """


    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    check_type(str, 'regex', regex, file)

    invalid = False
    logContent = ''

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return rows that not match regex pattern
        df = data[~data[column].map(str).str.match(rf"{regex}", na=False)]

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that not match to `{}` regex pattern: {} row(s)\n\n'.format(regex, len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Invalid regex pattern detected. View more in ' + file)
