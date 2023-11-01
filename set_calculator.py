import time
from colorama import Fore, Style, init, Back
import sys
# A calculator to calculate set
init()
class Cal:
    def __init__(self):
       self.pre() 
    def pre(self):    
        print("""
                CHOOSE THE NUMBER OF ELEMENTS YOU WANT IN A EACH SET
                1.) 2x2
                2.) 2x3
                3.) 3x2
                4.) 3x3
                5.) 3x4
                6.) 4x3
                7.) 4x4
        """)
        select = int(input("Select a number: "))

        if select == 1:
            self.one()
        elif select == 2:
            self.two() 
        elif select == 3:
            self.three()  
        elif select == 4:
            self.four()  
        elif select == 5:
            self.five() 
        elif select == 6:
            self.six()           
        elif select == 7:
            self.seven() 
        else:
            print("Invalid Input")
            self.pre()          

    # WHEN SELECT IS 1
    def one(self):        
            print("The First Set")
            inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")) }

            print("\nThe Second Set\n")
            inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")) }

            print("""
                    ENTER THE CALCULATION YOU WANT TO PERFORM
                    1.) Union of the set
                    2.) Intersection
                    3.) Difference
            """)
            user = int(input("Select a number: "))
            if user == 1:
                union = inp1.union(inp2)
                print(f'The union of {inp1} and {inp2} = {union}')
            elif user == 2:
                intersect = inp1.intersection(inp2)
                print(f'The intersection of {inp1} and {inp2} = {intersect}')
            elif user == 3:
                print("""
                        ENTER THE ONE TO FIND ITS DIFFERENCE:
                        1.) Set A - Set B
                        2.) Set B - Set A
                """)
                inner = int(input("Enter a number: "))
                if inner == 1:
                    difference1 = inp1.difference(inp2)
                    print(f'The differnce of {inp1} and {inp2} = {difference1}')
                elif inner == 2:    
                    difference2 = inp2.difference(inp1)
                    print(f'The differnce of {inp1} and {inp2} = {difference2}')
                else:
                    print("Invalid Input!") 
                    self.one() 
            self.another()          
            
    # WHEN SELECT IS 2 
    def two(self):
            print("The First Set")
            inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")) }

            print("\nThe Second Set\n")
            inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

            print("""
                    ENTER THE CALCULATION YOU WANT TO PERFORM
                    1.) Union of the set
                    2.) Intersection
                    3.) Difference
            """)
            user = int(input("Select a number: "))
            if user == 1:
                union = inp1.union(inp2)
                print(f'The union of {inp1} and {inp2} = {union}')
            elif user == 2:
                intersect = inp1.intersection(inp2)
                print(f'The intersection of {inp1} and {inp2} = {intersect}')
            elif user == 3:
                print("""
                        ENTER THE ONE TO FIND ITS DIFFERENCE:
                        1.) Set A - Set B
                        2.) Set B - Set A
                """)
                inner = int(input("Enter a number: "))
                if inner == 1:
                    difference1 = inp1.difference(inp2)
                    print(f'The differnce of {inp1} and {inp2} = {difference1}')
                elif inner == 2:    
                    difference2 = inp2.difference(inp1)
                    print(f'The differnce of {inp1} and {inp2} = {difference2}')
                else:
                    print("Invalid Input!")
                    self.two() 
            self.another()

    # WHEN SELECT IS 3 
    def three(self):
            print("The First Set")
            inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

            print("\nThe Second Set\n")
            inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: "))}

            print("""
                    ENTER THE CALCULATION YOU WANT TO PERFORM
                    1.) Union of the set
                    2.) Intersection
                    3.) Difference
            """)
            user = int(input("Select a number: "))
            if user == 1:
                union = inp1.union(inp2)
                print(f'The union of {inp1} and {inp2} = {union}')
            elif user == 2:
                intersect = inp1.intersection(inp2)
                print(f'The intersection of {inp1} and {inp2} = {intersect}')
            elif user == 3:
                print("""
                        ENTER THE ONE TO FIND ITS DIFFERENCE:
                        1.) Set A - Set B
                        2.) Set B - Set A
                """)
                inner = int(input("Enter a number: "))
                if inner == 1:
                    difference1 = inp1.difference(inp2)
                    print(f'The differnce of {inp1} and {inp2} = {difference1}')
                elif inner == 2:    
                    difference2 = inp2.difference(inp1)
                    print(f'The differnce of {inp1} and {inp2} = {difference2}')
                else:
                    print("Invalid Input!") 
                    self.three() 
            self.another()        

    # WHEN SELECT IS 4    
    def four(self):
            print("The First Set")
            inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

            print("\nThe Second Set\n")
            inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

            print("""
                    ENTER THE CALCULATION YOU WANT TO PERFORM
                    1.) Union of the set
                    2.) Intersection
                    3.) Difference
            """)
            user = int(input("Select a number: "))
            if user == 1:
                union = inp1.union(inp2)
                print(f'The union of {inp1} and {inp2} = {union}')
            elif user == 2:
                intersect = inp1.intersection(inp2)
                print(f'The intersection of {inp1} and {inp2} = {intersect}')
            elif user == 3:
                print("""
                        ENTER THE ONE TO FIND ITS DIFFERENCE:
                        1.) Set A - Set B
                        2.) Set B - Set A
                """)
                inner = int(input("Enter a number: "))
                if inner == 1:
                    difference1 = inp1.difference(inp2)
                    print(f'The differnce of {inp1} and {inp2} = {difference1}')
                elif inner == 2:    
                    difference2 = inp2.difference(inp1)
                    print(f'The differnce of {inp1} and {inp2} = {difference2}')
                else:
                    print("Invalid Input!") 
                    self.four()
            self.another()
                        
    # WHEN SELECT IS 5 
    def five(self):
            print("The First Set")
            inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

            print("\nThe Second Set\n")
            inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: ")), int(input("Enter the forth set: "))}

            print("""
                    ENTER THE CALCULATION YOU WANT TO PERFORM
                    1.) Union of the set
                    2.) Intersection
                    3.) Difference
            """)
            user = int(input("Select a number: "))
            if user == 1:
                union = inp1.union(inp2)
                print(f'The union of {inp1} and {inp2} = {union}')
            elif user == 2:
                intersect = inp1.intersection(inp2)
                print(f'The intersection of {inp1} and {inp2} = {intersect}')
            elif user == 3:
                print("""
                        ENTER THE ONE TO FIND ITS DIFFERENCE:
                        1.) Set A - Set B
                        2.) Set B - Set A
                """)
                inner = int(input("Enter a number: "))
                if inner == 1:
                    difference1 = inp1.difference(inp2)
                    print(f'The differnce of {inp1} and {inp2} = {difference1}')
                elif inner == 2:    
                    difference2 = inp2.difference(inp1)
                    print(f'The differnce of {inp1} and {inp2} = {difference2}')
                else:
                    print("Invalid Input!") 
                    self.five()
            self.another()         

    # WHEN SELECT IS 6 
    def six(self):
            print("The First Set")
            inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: ")), int(input("Enter the forth set: "))}

            print("\nThe Second Set\n")
            inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

            print("""
                    ENTER THE CALCULATION YOU WANT TO PERFORM
                    1.) Union of the set
                    2.) Intersection
                    3.) Difference
            """)
            user = int(input("Select a number: "))
            if user == 1:
                union = inp1.union(inp2)
                print(f'The union of {inp1} and {inp2} = {union}')
            elif user == 2:
                intersect = inp1.intersection(inp2)
                print(f'The intersection of {inp1} and {inp2} = {intersect}')
            elif user == 3:
                print("""
                        ENTER THE ONE TO FIND ITS DIFFERENCE:
                        1.) Set A - Set B
                        2.) Set B - Set A
                """)
                inner = int(input("Enter a number: "))
                if inner == 1:
                    difference1 = inp1.difference(inp2)
                    print(f'The differnce of {inp1} and {inp2} = {difference1}')
                elif inner == 2:    
                    difference2 = inp2.difference(inp1)
                    print(f'The differnce of {inp1} and {inp2} = {difference2}')
                else:
                    print("Invalid Input!")  
                    self.six() 
            self.another()        

    # WHEN SELECT IS 7
    def seven(self):
            print("The First Set")
            inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: ")), int(input("Enter the forth set: ")) }

            print("\nThe Second Set\n")
            inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: ")), int(input("Enter the forth set: ")) }

            print("""
                ENTER THE CALCULATION YOU WANT TO PERFORM
                1.) Union of the set
                2.) Intersection
                3.) Difference
                """)
            
            user = int(input("Select a number: "))
            if user == 1:
                union = inp1.union(inp2)
                print(f'The union of {inp1} and {inp2} = {union}')
            elif user == 2:
                intersect = inp1.intersection(inp2)
                print(f'The intersection of {inp1} and {inp2} = {intersect}')
            elif user == 3:
                print("""
                        ENTER THE ONE TO FIND ITS DIFFERENCE:
                        1.) Set A - Set B
                        2.) Set B - Set A
                """)
                inner = int(input("Enter a number: "))
                if inner == 1:
                    difference1 = inp1.difference(inp2)
                    print(f'The differnce of {inp1} and {inp2} = {difference1}')
                elif inner == 2:    
                    difference2 = inp2.difference(inp1)
                    print(f'The differnce of {inp1} and {inp2} = {difference2}')
                else:
                    print("Invalid Input!")
                    self.seven()
            self.another()        
    def another(self):
        print('1 for another calcution or 0 to exit')
        inp = input('Select: ')
        if inp == '1':
            self.pre()
        elif inp == '0':
            print('Exit!')

     

cal = Cal()