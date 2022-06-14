from Bookkeeping.application.salary import calculate_salary
from Bookkeeping.application.people import get_employees
import datetime

print(datetime.date.today())
if __name__ == '__main__':
    calculate_salary()
    get_employees()