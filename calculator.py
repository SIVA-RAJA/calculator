import numpy as np


class Calculator:
    
    def add(self, arr):
        sum = np.sum(arr)
        print(sum)
        
    def mul(self, arr):
        mul = np.prod(arr)
        print(mul)
        
    def div(self, arr1, arr2):
        div = np.divide(arr1,arr2)
        print(div)
        

c = Calculator()

print("\t\t\t______CALCULATOR______")

def user():
    
    while True:
        
        
        print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
        op = int(input("Enter the operation :"))
        
        if op == 1 or op == 2:
            func()
            c.add(arr)
            return next()
                
        elif op == 3:
            func()
            c.mul(arr)
            return next()
   
        elif op == 4:
            ar1 = input("enter numerator numbers :")
            ar2 = input("enter denominator numbers :")
            ar1 = np.array(ar1.split(" "))
            ar2 = np.array(ar2.split(" "))
            arr1 = ar1.astype(float)
            arr2 = ar2.astype(float)
            c.div(arr1,arr2)
            return next()
            
        
        else:
            print("Enter correct option")
            continue
        
def func():
    
    global arr
    ar = input("enter numbers :")
    ar = np.array(ar.split(" "))
    arr = ar.astype(float)
    
def next():
    
    ch = input("Do you want to continue (y/n) :")
    ch = ch.lower()
        
    if ch == "y":
        return user()
        
    elif ch == "n":
        return exit()
            
    else:
         
        opt = input("Enter correct option (y/n) :")
        opt = opt.lower()
            
        if opt == "y":
            return user()
                
        else:
            return None
        
def exit():
    print("EXITING............")
    return None


if __name__ == "__main__":
        
        user()
        
        
    