import numpy as np


class Calculator:
    
    def add(self, arr):
        sum = np.sum(arr)
        print(sum)
        

c = Calculator()

def user():
 
    print("______CALCULATOR______")
    print("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
    op = int(input("Enter the operation :"))
    
    if op == 1:
        func()
        c.add(arr)
    
    elif op == 2:
        pass
        
    elif op == 3:
        pass
        
    elif op == 4:
        pass
        
    else:
        print("Enter correct option")
        
def func():
    
    global arr
    ar = input("enter numbers :")
    ar = np.array(ar.split(" "))
    arr = ar.astype(float)
    


if __name__ == "__main__":
        
        user()
        
        
    