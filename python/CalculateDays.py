#Program to calculate number of days between two dates.

import datetime
from datetime import date
First_date =date(2019, 4, 11)
Second_date = date(2019, 4, 9)
result = First_date - Second_date
print(result.days)


