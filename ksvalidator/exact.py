import pandas as pd
from .functions import check_type, check_column, log


def exact(data, targetColumn, condition, file = 'Error_Log'):
    """
    Exact validation\n
    data: Data source for validation\n
    targetColumn: Column name that requires for validation \n
    condition: Exact condition (Support multiple conditions by delimiter (,) E.g. A,B,C)\n
    file: Invalid output text file name. E.g. ".\\Output\\Error_Log" store log with Error_Log name in Output folder
    """
    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    check_type(str, 'condition', condition, file)

    invalid = False
    logContent = ''

    strConditions = condition.replace(',', '|')

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return rows that not equat to 'condition'
        df = data[~data[column].map(str).str.fullmatch(strConditions, na=False)]

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that not equal to `{}`: {} row(s)\n\n'.format(condition, len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Invalid exact detected.')
