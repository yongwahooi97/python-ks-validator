import pandas as pd
from .functions import check_type, check_column, log

def regex(data, targetColumn, regex, file = 'Error_Log'):
    """
    Regular expression validation
    https://regex101.com/\n
    Support multiple condition by delimiter (,) E.g. A,B,C\n
    data: Data source for validation\n
    targetColumn: Column name that requires for validation\n 
    regex: Regular expression pattern\n
    file: Invalid output text file name. E.g. ".\\Output\\Error_Log" store log with Error_Log name in Output folder
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
        raise Exception('Invalid regex pattern detected.')
