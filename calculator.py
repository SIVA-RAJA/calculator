import numpy as np


class Calculator:
    """A calculator class that performs basic arithmetic operations on arrays."""
    
    def add(self, numbers):
        """
        Calculate the sum of numbers in an array.
        
        Args:
            numbers: Array of numbers to add
            
        Returns:
            The sum of all numbers
        """
        return np.sum(numbers)
        
    def subtract(self, numbers):
        """
        Calculate the result of subtracting all subsequent numbers from the first.
        
        Args:
            numbers: Array of numbers where first number is minuend
            
        Returns:
            The result of subtraction
        """
        if len(numbers) == 0:
            return 0
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result
        
    def multiply(self, numbers):
        """
        Calculate the product of numbers in an array.
        
        Args:
            numbers: Array of numbers to multiply
            
        Returns:
            The product of all numbers
        """
        return np.prod(numbers)
        
    def divide(self, numerators, denominators):
        """
        Perform element-wise division of numerators by denominators.
        
        Args:
            numerators: Array of numerator values
            denominators: Array of denominator values
            
        Returns:
            Array of division results
            
        Raises:
            ValueError: If any denominator is zero
        """
        if np.any(denominators == 0):
            raise ValueError("Cannot divide by zero")
        return np.divide(numerators, denominators)
        


def get_numbers_from_input(prompt):
    """
    Get an array of numbers from user input.
    
    Args:
        prompt: The prompt message to display
        
    Returns:
        numpy array of float numbers
        
    Raises:
        ValueError: If input cannot be converted to numbers
    """
    user_input = input(prompt)
    numbers_str = user_input.split()
    numbers = np.array([float(num) for num in numbers_str])
    return numbers


def display_menu():
    """Display the calculator menu options."""
    print("\n" + "="*40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("="*40)


def ask_continue():
    """
    Ask user if they want to continue.
    
    Returns:
        True if user wants to continue, False otherwise
    """
    while True:
        choice = input("\nDo you want to continue (y/n): ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter 'y' or 'n'")


def main():
    """Main function to run the calculator application."""
    calculator = Calculator()
    
    print("\n" + " "*15 + "CALCULATOR" + " "*15)
    
    while True:
        try:
            display_menu()
            operation = int(input("Enter the operation (1-5): "))
            
            if operation == 5:
                print("\nExiting calculator. Goodbye!")
                break
            
            if operation == 1:
                numbers = get_numbers_from_input("Enter numbers separated by spaces: ")
                result = calculator.add(numbers)
                print(f"\nResult: {result}")
                
            elif operation == 2:
                numbers = get_numbers_from_input("Enter numbers separated by spaces: ")
                result = calculator.subtract(numbers)
                print(f"\nResult: {result}")
                
            elif operation == 3:
                numbers = get_numbers_from_input("Enter numbers separated by spaces: ")
                result = calculator.multiply(numbers)
                print(f"\nResult: {result}")
                
            elif operation == 4:
                numerators = get_numbers_from_input("Enter numerator numbers separated by spaces: ")
                denominators = get_numbers_from_input("Enter denominator numbers separated by spaces: ")
                
                if len(numerators) != len(denominators):
                    print("\nError: Number of numerators and denominators must be equal")
                    continue
                    
                result = calculator.divide(numerators, denominators)
                print(f"\nResult: {result}")
                
            else:
                print("\nInvalid option! Please enter a number between 1 and 5.")
                continue
            
            if not ask_continue():
                print("\nExiting calculator. Goodbye!")
                break
                
        except ValueError as e:
            print(f"\nError: {e}")
            print("Please enter valid numbers.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
        
        
    