#simple script for printing total days between two dates

import datetime
def count_date(year, month, day):
    current_date = datetime.date.today()
    input_date = datetime.date(year, month, day)
    difference_date = str(input_date-current_date).split(",")
    print("Difference date is: {}".format(difference_date[0]))
    
def run():
    enter_date = input("Enter a date, each element must be separated by hyphens: ")
    enter_date_list = list(map(int, enter_date.split("-")))
    count_date(enter_date_list[0], enter_date_list[1], enter_date_list[2])

if __name__ == '__main__':
    run()