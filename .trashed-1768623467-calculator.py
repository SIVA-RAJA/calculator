import numpy as np


class Calculator:
    
    def add(self, arr):
        sum = np.sum(arr)
        print(sum)
        
    def mul(self, arr):
        mul = np.prod(arr)
        print(mul)
        

c = Calculator()

print("\t\t\t______CALCULATOR______")

def user():
    
    while True:
        
        
        print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
        op = int(input("Enter the operation :"))
        
        if op == 1 or op == 2:
            func()
            c.add(arr)
            next()
                
        elif op == 3:
            func()
            c.mul(arr)
            next()
   
        elif op == 4:
            pass
        
        else:
            print("Enter correct option")
            continue
        
def func():
    
    global arr
    ar = input("enter numbers :")
    ar = np.array(ar.split(" "))
    arr = ar.astype(float)
    
def next():
    
    while True:
        ch = input("Do you want to continue (y/n) :")
        ch = ch.lower()
        
        if ch == "y":
            user()
            break
            
        elif ch == "n":
            exit()
            break
            
        else:
            opt = input("Enter correct option (y/n) :")
            opt = opt.lower()
            
            if opt == "y":
                user()
                break
                
            else:
                break
        
def exit():
    print("EXITING............")
    return None


if __name__ == "__main__":
        
        user()
        
        
    