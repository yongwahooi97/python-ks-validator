import pandas as pd
import numpy as np
from datetime import datetime
from .functions import check_type, check_column, log, validate_date

def date_format(data, targetColumn, format, file = 'Error_Log.txt'):
    
    """
    Date format validation\n
    Raise error when data does not match 'format'.\n
    Invalid data will store in text file with location and name that declared in 'file'.\n

    Parameters:
    data (pd.DataFrame): Data source for validation
    targetColumn (list): Column name that requires for validation
    format (str): Date format (https://www.geeksforgeeks.org/python-datetime-strptime-function/)
    file (str): Invalid output text file.  
    
    Raises:
    TypeError: if parameters invalid type
    Exception: if invalid data detected
    """

    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    check_type(str, 'format', format, file)

    invalid = False
    logContent = ''

    # Functions to verify the date format
    def strftime_format(value, format):
        try:
            datetime.strptime(value, format)
        except ValueError:
            return False
        return True

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return rows that not match date format
        df = data[~data.apply(lambda x: strftime_format(str(x[column]), format), axis=1)]

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that not match `{}` date format: {} row(s)\n\n'.format(format, len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Invalid date format detected.')

def date_range(data, targetColumn, format  = '%d/%m/%Y', startDate = np.nan, endDate = np.nan, file = 'Error_Log.txt'):
    
    """
    Date range validation\n
    Raise error when date does not within range.\n
    Invalid data will store in text file with location and name that declared in 'file'.\n

    Parameters:
    data (pd.DataFrame): Data source for validation
    targetColumn (list): Column name that requires for validation
    format (str): Date format. Default format is %d/%m/%Y (https://www.geeksforgeeks.org/python-datetime-strptime-function/)
    startDate (str): Data must after or on startDate. If none, leave it blank or set to np.nan\n
    endDate (str): Data must before or on endDate. If none, leave it blank or set to np.nan\n
    file (str): Invalid output text file.  
    
    Raises:
    TypeError: if parameters invalid type
    Exception: if invalid data detected
    """

    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    check_type(str, 'format', format, file)
    if not pd.isnull(startDate):
        validate_date('startDate', startDate, format, file)
    if not pd.isnull(endDate):
        validate_date('endDate', endDate, format, file)

    invalid = False
    logContent = ''

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return rows that not match date range
        df = data
        newColumn = 'new_' + column
        
        # Convert date to %d/%m/%Y format
        df[newColumn] = pd.to_datetime(df[column], dayfirst=True,  errors='coerce')
        df[newColumn] = pd.to_datetime(df[newColumn], dayfirst=True,  format=format, errors='coerce')

        desc = ''
        if pd.isnull(startDate) & pd.isnull(endDate):
            df = pd.DataFrame()
        elif pd.isnull(startDate):
            df = data[~(data[newColumn] <= endDate)]
            desc = 'before or equal to {}'.format(endDate)
        elif pd.isnull(endDate):
            df = data[~(data[newColumn] >= startDate)]
            desc = 'after or equal to {}'.format(startDate)
        else:
            df = data[~((data[newColumn] >= startDate) & (data[newColumn] <= endDate))]
            desc ='between {} and {}'.format(startDate, endDate)
        
        df = df.drop([newColumn], axis=1)

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that not {} date range: {} row(s)\n\n'.format(desc, len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Invalid date range detected. View more in ' + file)
