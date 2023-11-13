


from datetime import datetime
from datetime import date

months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
thdty = [4,6,9,11]
thrtyone = [1,3,5,7,8,10,12]
eght = [2]


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month
    
def diff_day(d1,d2):
    return d1.day-d2.day

def diffy_day(d1, d2):
    if d2.month in thrtyone:
        return (31-d2.day)+d1.day
    elif d2.month in thdty:
        return (30-d2.day)+d1.day
    else:
        return (28-d2.day)+d1.day
    
    
    

    
    

class Bank:
    def __init__(self):
        self.initial = 0
        self.money_target = 0
        self.date_start = None
        self.date_end = None

    

    def setTargetMoney(self):
        print("Set target money")
        money_target = int(input("Enter target money: "))
        self.money_target = money_target
        self.initial = int(input("Enter typical monthly wage: "))
        
        if self.money_target <= self.initial:
            print("You have already succeeded your target money!! ")
            answer = input("Do you still want to use the calculator?: ")
            if answer == 'yes':
                x.setTargetMoney()
            else: 
                print("Sorry we could not help you TT")
                exit()
           
                    
        else:
            answer = input("Do you want set date start?(yes/no) : ")
            if answer == 'yes':
                year = int(input("Enter Year : "))
                month = int(input("Enter Month : "))
                date_input = int(input("Enter Date : "))
                date_time = date(year, month, date_input)
                self.date_start = date_time
            elif answer =='no':
                self.date_start = date.today()
            else:
                print("Please enter yes or no ")
                x.setTargetMoney()

    def setDeadLine(self):
        print("Set a deadline")
        year = int(input("Enter Year : "))
        month = int(input("Enter Month : "))
        date_input = int(input("Enter Date : "))
        date_time = date(year, month, date_input)
        self.date_end = date_time



    def output(self):
        print("---------------------------")
        print("Target money: ", self.money_target)
        print("Date start: ", self.date_start)
        print("Date end: ", self.date_end)

        
        month_diff = diff_month(self.date_end, self.date_start)
        
        if month_diff ==0:
            day_diff = diff_day(self.date_end, self.date_start)
        else:
            day_diff = diffy_day(self.date_end, self.date_start)

        day_difference = 0

        if self.date_end.year==self.date_start.year:
            for _ in range(self.date_start.month+1,self.date_end.month):
                day_difference = day_difference +months[_]
        elif self.date_end.year>self.date_start.year:
                for _ in range(self.date_start.month+1,13):
                    day_difference = day_difference+months[_]
                for _ in range(1,self.date_end.month):
                    day_difference = day_difference+months[_]
        
       
        
        day_difference = day_difference+day_diff
        
        print(day_difference," days left before deadline !!")
        print("---------------------------")
        
        if day_difference<30:
            day_diff = diff_day(self.date_end, self.date_start)
            keep_per_day = (int(self.money_target)-int(self.initial))/day_difference
            keep_per_month = 0
            keep_per_year = 0
        else:
            keep_per_day = int(self.money_target) / day_difference
            keep_per_month = int(self.money_target) / (day_difference/30)
            keep_per_year = int(self.money_target) / (day_difference/365)
        
        if 1<=(day_difference/30)<=12 :
            interest = 1.004 
            n = self.money_target/((self.initial)*((interest)**(day_difference//30)))
            keep_per_day = ((n*self.initial)-self.initial)
            if n<1:
                print("Keep this monthly wages, no need to worry")
                k = input("Do you wish to start over? ")
                if k=='yes':
                    x.setTargetMoney()
                elif k=='no':
                    print('This is the end of the simulation')
                    exit()
            print("You still need extra ฿", round(keep_per_day/day_difference,2), " per day")
            if (day_difference/30)<=1:
                print("You need to find anonther", round(keep_per_day,2), " to acheive in a month")
            
            else: 
                print("You still need ฿",round(keep_per_day/month_diff,2),"per month")




        elif day_difference/30 >= 12:
             interest = 1.05
             if (day_difference/30)*(self.initial)>self.money_target:
                print("Your wage exceeds your target amount")
                print("This is recommended amount that will acheive your goal")
                l = self.money_target/((interest**(day_difference//365)))
                
                print("Keep per day: ", round((l/day_difference),2))
                print("Keep per month: ", round((l/(day_difference/30)),2))
                print("Keep per year: ", round((l/(day_difference/365)),2))
                

             else:
                    print("Inorder to acheive target goal you must keep more money")
                    extra = self.money_target/((self.initial)*((interest)**(day_difference//365)))
                    keep_per_day = ((extra*self.initial)-self.initial)
                    
                    print("Keep per day: ", round(keep_per_day/day_difference,2))
                    print("Keep per month: ", round(keep_per_day/(day_difference/30),2))
                    print("Keep per year: ", round(keep_per_day/(day_difference/365),2))
                
           
             
        else:
            print("You need",round((keep_per_day),2), "per day.")

        print("Thank you for using our service")

answer = 'yes'

while True:
    if answer == 'yes':
        x = Bank()
        x.setTargetMoney()
        x.setDeadLine()
        x.output()

        answer = input("Do you want to continue? (yes/no) : ")
        if answer == 'no':
            print("This is the end of the simulation")
            break
        elif answer == 'yes':
            continue
        
    

        

