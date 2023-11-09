# JAMES MOSETI MOTURI SCT211-0095/2022

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

userName = input("What is your name: ")

while True:
  print(f"Hello {userName}, welcome to our simple calculator")
  choice = int(input("""What kind of calculation do you want to perform from the list below:-
  1. Addition
  2. Multiplication
  3. Subtraction
  4. Division
  Enter a digit between 1-4?(0 to exit): """))

  if(choice == 1):
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    myCalc = Calculator(num1, num2)
    sum = myCalc.add()
    print(f"The sum of {num1} and {num2} is = {sum}")

  elif(choice == 2):
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    myCalc2 = Calculator(num1, num2)
    product = myCalc2.multiply()
    print(f"The product of {num1} and {num2} is = {product}")

  elif(choice == 3):
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    myCalc3 = Calculator(num1, num2)
    difference = myCalc3.subtract()
    print(f"The difference between {num1} and {num2} is = {difference}")

  elif(choice == 4):
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    myCalc4 = Calculator(num1, num2)
    quotient = myCalc4.divide()
    print(f"The result of dividing {num1} by {num2} is = {quotient}")

  elif(choice == 0):
    break

  else:
    print(f"{userName} you have made an invalid selection! Try again ")