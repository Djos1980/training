# Import date modules
from datetime import date
from dateutil.relativedelta import relativedelta

# Define type of IP and calculate filing deadline
IP = input("Please enter type of patent (PCT, Direct, EP Validation): ")
# Define the the deadline based on client input
if IP == "PCT":
    priority = input("Please enter the earliest priority date YYYY-MM-DD: ")
    year, month, day = map(int, priority.split('-'))  # split response and map
    priority = date(year, month, day)  # convert response to date
    deadline = priority + relativedelta(months=30)
    print('Filing deadline is ' + str(deadline))

elif IP == "Direct":
    priority = input("Please enter the earliest priority date YYYY-MM-DD: ")
    year, month, day = map(int, priority.split('-'))  # split response and map
    priority = date(year, month, day)
    deadline = priority + relativedelta(months=12)
    print('Filing deadline is ' + str(deadline))

elif IP == "EP Validation":
    priority = input("Please enter the grant date YYYY-MM-DD: ")
    year, month, day = map(int, priority.split('-'))  # split response and map
    priority = date(year, month, day)
    deadline = priority + relativedelta(months=3)
    print('Validation deadline is ' + str(deadline))
