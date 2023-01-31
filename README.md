# KSValidator

KSValidator is a Python package that contains several validation functions that use to validate data to ensure the quality of data and data are in correct format before proceed to next step.

## Installation and updating

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install KSValidator like below.
Rerun this command to check for and install updates .

```bash
pip install git+https://github.com/yongwahooi97/python-ks-validator.git
```

Uninstall KSValidator

```bash
pip uninstall ksvalidator
```

## Usage

Features:

-   unique: Validate the uniqueness of the value of the column
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   file: Invalid output text file name
-   require: Validate the null or empty value of the column
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   file: Invalid output text file name
-   start_with: Validate the value of the column must start with specific string
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   condition: Start with condition (Support multiple conditions by delimiter (,) E.g. A,B,C)
    -   file: Invalid output text file name
-   end_with: Validate the value of the column must end with specific string
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   condition: End with condition (Support multiple conditions by delimiter (,) E.g. A,B,C)
    -   file: Invalid output text file name
-   contains: Validate the value of the column must contains specific string
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   condition: Contains condition (Support multiple conditions by delimiter (,) E.g. A,B,C)
    -   file: Invalid output text file name
-   exact: Validate the value of the column must equal to specific string
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   condition: Exact condition (Support multiple conditions by delimiter (,) E.g. A,B,C)
    -   file: Invalid output text file name
-   regex: Validate the value of the column must match regular expression
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   regex: Regular expression pattern. [Online regex test](https://regex101.com/)
    -   file: Invalid output text file name
-   number: Validate the value of the column within given range
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   min: Minimum value of data. If none, leave it blank or set to np.nan.
    -   max: Minimum value of data. If none, leave it blank or set to np.nan.
    -   file: Invalid output text file name
-   date_format: Validate the value of the column within given range
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   format: [Date format](https://www.geeksforgeeks.org/python-datetime-strptime-function/)
    -   file: Invalid output text file name
-   date_range: Validate the value of the column within given range
    -   data: Data source for validation
    -   targetColumn: Column name(s) that requires for validation
    -   format: [Date format](https://www.geeksforgeeks.org/python-datetime-strptime-function/)
    -   startDate: Data must after or on startDate. If none, leave it blank or set to np.nan.
    -   endDate: Data must before or on endate. If none, leave it blank or set to np.nan.
    -   file: Invalid output text file name

#### Demo of some of the features:

```python
import pandas as pd
import ksvalidator
from ksvalidator import unique

df = pd.DataFrame({'ID': [1, 2, 2], 'Name': ['Alex', 'Sam', 'Ella']})
unique(df, ['ID'])
```

Others demo can view in [test](/test/) folder
