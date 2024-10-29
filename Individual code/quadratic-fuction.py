import time
import random
import math

#for now, it is solving quadratic equation only

#defining the first random excuse
time_sleep = [0.7,0.5,1,0.3,1.2] 
def first_overthinker_random():
    excuses = [
    "Hmm, let me think about this for a second...\n",
    "Are you sure this is the right problem to solve?\n",
    "Wait, let's consider all possible scenarios first...\n",
    "This feels more complex than it seems.\n",
    "Okay, hold on, this might take a while...\n"
    ]
    
    excuse_1 = random.choice(excuses)
    time.sleep(0.7)
    
    print(excuse_1)
    
def calculating_discriminant():
    thinking_prompts = [
    "Analyzing this carefully...\n",
    "This needs a bit more attention...\n",
    "Let’s not rush through this...\n",
    "Making sure everything adds up...\n",
    "Processing... slowly but surely...\n",
    "Taking my time with this one...\n",
    "Breaking it down step by step...\n",
    "Giving this problem the attention it deserves...\n",
    "Double-checking all possibilities...\n",
    "Thinking deeply... almost there...\n",
    "Considering every detail...\n",
    "Going through all the scenarios...\n",
    "Taking a moment to reflect...\n",
    "Carefully piecing things together...\n",
    "Digging into the details...\n"
    ] 
    
      
    for i in range(4):
        prompt = random.choice(thinking_prompts)
        
        time_random = random.choice(time_sleep)
        
        print(prompt)
        time.sleep(time_random)
        
        thinking_prompts.remove(prompt)
        
def thinking_before_discriminant():
    discriminant_thinking_prompts = [
        "Calculating the discriminant...\n",
        "Breaking down the b² part...\n",
        "Multiplying 4 with 'a' and 'c'...\n",
        "Subtracting the results carefully...\n",
        "Evaluating b² - 4ac now...\n",
        "Checking if the discriminant is positive...\n",
        "This looks like a quadratic case...",
        "Balancing the equation...\n",
        "Almost done with b² - 4ac...\n",
        "Finalizing the discriminant...\n",
        "Carefully evaluating each step...\n",
        "Working through b², 4ac...\n",
        "Getting closer to the final result...\n",
        "Just about ready to solve for roots...\n",
        "Wrapping up the discriminant calculation...\n"
    ]
    time_random = random.choice(time_sleep)
    
    
    for i in range(2):
        random_prompt = random.choice(discriminant_thinking_prompts)
        print(random_prompt)
        discriminant_thinking_prompts.remove(random_prompt)
        time.sleep(time_random)
    
    

    
    
   
#intro    
 

print("This program solves quadratic equations of the form ax^2 + bx + c = 0.")
print("You will need to input the values for a, b, and c, where:")
print("  - a is the coefficient of x^2 (quadratic term)")
print("  - b is the coefficient of x (linear term)")
print("  - c is the constant term\n")


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))



print("Now calculating the discriminant...") 
thinking_before_discriminant() 
discriminant = b**2 - 4*a*c





if(discriminant >= 0):
    
    print(f"Discriminant is {discriminant}")
    user_input_after_discriminant = input("Type any key to proceed further:")
    print(" ")
    

    root1 = -b + math.sqrt(discriminant) / 2 * a

    root2 = -b - math.sqrt(discriminant) / 2 * a
    
    first_overthinker_random()
    time.sleep(0.7)
    calculating_discriminant()
    
    
    print(f"\nRoots of quadratic equation are",end = " ")
    time.sleep(0.5)
    print(f"{root1} and", end = " ")
    time.sleep(0.3)
    print(f"{root2}")
    
    
else:
    print("Discriminant is negative so no real roots")



