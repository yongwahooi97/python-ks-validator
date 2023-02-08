from datetime import datetime

# Check data type for function argument/ parameters
def check_type(dataType, key, value, file):
    if not isinstance(value, dataType):
        error_msg = 'Variable `' + str(key) + '` should be type ('
        error_msg += str(dataType) + ') but instead is type (' + str(type(value)) + ')'
        log(file, error_msg)
        raise TypeError(error_msg)

def validate_date(key, date, format, file):
    try:
        datetime.strptime(date, format)
    except ValueError:
        error_msg = 'Variable `' + str(key) + '` should be in ' + format
        error_msg += ' but it is ' + date
        log(file, error_msg)
        raise ValueError("Incorrect data format, should be in " + format)

# Check column name in data
def check_column(column, data, file):
    if column not in data.columns:
        log(file, "Column not found: " + column)
        raise Exception('Column not found: ' + column)

# Log file to text file
def log(file, content):
    try:
        date = datetime.now()
        f = open(file, "a")
        print('\n========================\n', file=f)
        print('Date: '+ date.strftime("%d/%m/%y") + '\nTime: ' + date.strftime("%X"), file=f)
        print('\n------------\n', file=f)
        print(content, file=f)
        print('\n========================\n', file=f)
        f.close()
    except IOError as e:
        f = open('Error_Log.txt', "a")
        print(e, file=f)
        f.close()
        raise e