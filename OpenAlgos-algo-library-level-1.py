import time
import random

#for now, it is solving quadratic equation only

#defining the first random excuse
def first_overthinker_random():
    excuses = [
    "Hmm, let me think about this for a second...",
    "Are you sure this is the right problem to solve?",
    "Wait, let's consider all possible scenarios first...",
    "This feels more complex than it seems.",
    "Okay, hold on, this might take a while..."
    ]
    
    excuse_1 = random.choice(excuses)
    time.sleep(0.7)
    
    print(excuse_1)
    
    
def solve_quadratic():
    # Intro explaining the coefficients
    print("This program solves quadratic equations of the form ax^2 + bx + c = 0.")
    print("You will need to input the values for a, b, and c, where:")
    print("  - a is the coefficient of x^2 (quadratic term)")
    print("  - b is the coefficient of x (linear term)")
    print("  - c is the constant term\n")

    # Input coefficients
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    discriminant = b**2 - 4*a*c
    
    
   
#intro    
print("What are we solving today?")
print("1)Quadratic Equation")
user_input = int(input("Type the number before the operation you need to solve"))


#if-elif statements
if(user_input == 1):
    print("")
   