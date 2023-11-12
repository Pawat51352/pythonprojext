

from datetime import datetime
from datetime import date

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def diff_day(d1, d2):
    return d1.day - d2.day


class Bank:
    def __init__(self):
        self.money_target = 0
        self.date_start = None
        self.date_end = None

    def setTargetMoney(self):
        print("Set target money")
        money_target = int(input("Enter target money: "))
        self.money_target = money_target
        answer = input("Do you want set date start?(y/n) : ")
        if answer == 'y':
            year = int(input("Enter Year : "))
            month = int(input("Enter Month : "))
            date_input = int(input("Enter Date : "))
            date_time = date(year, month, date_input)
            self.date_start = date_time
        elif answer =='n':
            self.date_start = date.today()
        else:
            print("Please enter y or n ")
            x.setTargetMoney()

    def setDeadLine(self):
        print("Set a deadline")
        year = int(input("Enter Year : "))
        month = int(input("Enter Month : "))
        date_input = int(input("Enter Date : "))
        date_time = date(year, month, date_input)
        self.date_end = date_time

    def output(self):
        print("Target money: ", self.money_target)
        print("Date start: ", self.date_start)
        print("Date end: ", self.date_end)

        
        month_diff = diff_month(self.date_end, self.date_start)

        if month_diff == 0:
            day_diff = diff_day(self.date_end, self.date_start)
            keep_per_day = int(self.money_target) / day_diff
            keep_per_month = 0
            keep_per_year = 0
        else:
            keep_per_day = int(self.money_target) / month_diff / 30
            keep_per_month = int(self.money_target) / month_diff
            keep_per_year = int(self.money_target) / month_diff * 12

        if month_diff >= 1 and month_diff < 12:
            interest = self.money_target * 0.004 * month_diff
            print("Keep per day: ", keep_per_day)
            print("Keep per month: ", keep_per_month)
            print("Interest: ", interest)

        elif month_diff >= 12:
            interest = self.money_target * 0.05 * (month_diff / 12)
            print("Keep per day: ", keep_per_day)
            print("Keep per month: ", keep_per_month)
            print("Keep per year: ", keep_per_year)
            print("Interest: ", interest)
        else:
            print("Keep per day: ", keep_per_day)

        print("Thank you for using our service")

answer = 'y'

while True:
    if answer == 'y':
        x = Bank()
        x.setTargetMoney()
        x.setDeadLine()
        x.output()

        answer = input("Do you want to continue? (y/n) : ")
        if answer == 'n':
            print("This is the end of the simulation")
            break
        elif answer == 'y':
            continue
        else:
            print("Please enter y or n")
            continue
    

        




