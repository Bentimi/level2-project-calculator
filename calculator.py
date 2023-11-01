import time
from math import tan, sin, cos, pi
class Calculator:
    def __init__(self):
        print("""
                WHICH OPERATION DO YOU WANT TO PERFORM?
                1. Addition
                2. Subtraction
                3. Division
                4. Multiplication
                5. More
        """)
        self.page()
    def page(self): 
        self.val = int(input("Option: "))
        if self.val == 5:
            self.second()
        elif self.val == 1:
            self.first()
            self.add()
        elif self.val == 2:
            self.first()
            self.sub()
        elif self.val == 3:
            self.first()
            self.divide()
        elif self.val == 4:
            self.first()
            self.mult()
        else:
            print("Invalid Option")
            self.__init__()    


    def first(self):    
        # print("This calculator can perform simple calculations.")
        self.inp1 = float(input("Frst Value: "))
        self.inp2 = float(input("Second Value: "))
        print("Loading...")
        time.sleep(3)
    def second(self):
        self.dividend = float(input("Dividend/First Vale: "))
        self.divisor = float(input("Divisor/Total Value: "))
        print("Loading...")
        time.sleep(3)
        print("""
                 WHICH OPERATION DO YOU WANT TO PERFORM?
                1. Percetage
                2. Modulus 
        """)
        self.user = int(input("Option: "))
        if self.user == 1:
            self.percent()
        elif self.user == 2:
            self.mod()
        else:
            print("Try Again")
            self.__init__()   

        # self.dividend = float(input("DIVIDEND: "))
        # self.divisor = float(input("DIVISOR: "))
        # print("Loading...")
        # time.sleep(3)
        # # print("")         

    def add(self):
        self.addd = self.inp1 + self.inp2
        print("Loading...")
        time.sleep(2)
        print(f"{self.inp1} + {self.inp2} = {self.addd}")    
    def sub(self):
        self.subb = self.inp1 - self.inp2
        print("Loading...")
        time.sleep(2)
        print(f"{self.inp1} - {self.inp2} = {self.subb}")    
    def divide(self):
        self.division = self.inp1 / self.inp2
        print("Loading...")
        time.sleep(2)
        print(f"{self.inp1} / {self.inp2} = {self.division}")   
    def mult(self):
        self.multt = self.inp1 * self.inp2
        print("Loading...")
        time.sleep(2)
        print(f"{self.inp1} * {self.inp2} = {self.multt}")    
    def percent(self):
        self.percentage = (self.dividend / self.divisor)*100
        print("Loading...")
        time.sleep(2)
        print(f"ANS: {self.percentage}%")   
    def mod(self):
        self.modd = self.dividend % self.divisor
        print("Loading...")
        time.sleep(2)
        print(f"The mod of {self.dividend} and {self.divisor} is {(self.modd)}")   
         
cal = Calculator()
# print(f"{cal.page()}")
