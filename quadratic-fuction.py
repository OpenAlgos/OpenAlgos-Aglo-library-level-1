import time
import random
import math

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
    
def calculating_discriminant():
    thinking_prompts = [
    "Hmm, let me analyze these numbers for a moment... They seem simple, but looks can be deceiving.",
    "Okay, plugging these into the formula... but wait, should I double-check? Nah, let's keep going.",
    "Calculating the discriminant... this could take a second. Or maybe more. Let's not rush this.",
    "Alright, I'm breaking it down. Step by step... there's no room for errors here.",
    "Wait a minute... am I missing something? No, I think we're good. Let's move forward.",
    "Reevaluating all possible scenarios... what if 'a' was 0? Oh, never mind, that would be a different equation.",
    "Discriminant formula... right... b² minus 4ac. Yeah, that looks good. But let me run it again, just to be sure.",
    "Crunching the numbers... carrying the one... wait, there’s no one to carry. Focus!",
    "This part feels tricky, but we can handle it... just gotta keep my mind on the discriminant.",
    "Almost there, I can feel the answer coming... it’s close. Very close.",
    "Running some extra checks... just in case the math gods are testing my patience.",
    "Is this taking too long? Or is it the perfect amount of time to give you an accurate answer?",
    "Considering every possible outcome... but I guess only one matters here.",
    "Cross-referencing previous calculations... okay, maybe not, but it sounds smart.",
    "Evaluating the situation... recalculating... okay, I think I’ve got it."
    ]    
    prompts = random.choice(thinking_prompts)
    time.sleep(0.7)
    print(prompts)
    

    
    
   
#intro    
 

print("This program solves quadratic equations of the form ax^2 + bx + c = 0.")
print("You will need to input the values for a, b, and c, where:")
print("  - a is the coefficient of x^2 (quadratic term)")
print("  - b is the coefficient of x (linear term)")
print("  - c is the constant term\n")


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
calculating_discriminant()
    
discriminant = b**2 - 4*a*c
if(discriminant >= 0):

    root1 = -b + math.sqrt(discriminant) / 2 * a

    root2 = -b - math.sqrt(discriminant) / 2 * a
    
else:
    print("No real root")



