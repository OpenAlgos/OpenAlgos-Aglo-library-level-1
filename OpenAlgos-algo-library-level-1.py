#welcome to OpenAlgos algorithm library level 1
import time

import random
import math
def solve_quadratic():
    #by Shardul Funde
    #for now, it is solving quadratic equation only

    #defining the first random excuse
    time_sleep = [0.7,0.5,1,0.3,1.2] 
    
    #defining the first random excuse
    def first_overthinker_random():
        excuses = [
        "Hmm, let me think about this for a second...\n",
        "Are you sure this is the right problem to solve?\n",
        "Wait, let's consider all possible scenarios first...\n",
        "This feels more complex than it seems.\n",
        "Okay, hold on, this might take a while...\n",
        "I need to double-check my calculations...\n",
        "This requires some deep thinking...\n",
        "Let me ponder over this for a moment...\n",
        "I need to make sure I get this right...\n",
        "This is a tough one, give me a second...\n",
        "I need to analyze this from all angles...\n",
        "This might take some extra time...\n",
        "I need to ensure every detail is correct...\n",
        "Let me take a closer look at this...\n",
        "I need to think this through carefully...\n"
        ]
        
        excuse_1 = random.choice(excuses)
        time.sleep(0.7)
        
        print(excuse_1)
    #defining the second random excuse    
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
        
        #randomly selecting the prompt
        for i in range(4):
            prompt = random.choice(thinking_prompts)
            
            time_random = random.choice(time_sleep)
            
            print(prompt)
            time.sleep(time_random)
            
            thinking_prompts.remove(prompt)
    #defining the third random excuse        
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
    
#by Shardul Funde
    print("Welcome to the Thinking Calculator!")
    print("This program solves quadratic equations of the form ax^2 + bx + c = 0.")
    print("You will need to input the values for a, b, and c, where:")
    print("  - a is the coefficient of x^2 (quadratic term)")
    print("  - b is the coefficient of x (linear term)")
    print("  - c is the constant term\n")


    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))


    #calculating the discriminant
    print("Now calculating the discriminant...") 
    thinking_before_discriminant() 
    discriminant = b**2 - 4*a*c





    if(discriminant >= 0):
        
        print(f"Discriminant is {discriminant}")
        user_input_after_discriminant = input("Type any key to proceed further:")
        print(" ")
        
        #calculating roots
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
        
def college_ranker():
        # Lists to store college names, ratings, and rankings
        #by shardul funde
        l = []
        college_ratings = []
        college_ranking = []

        # Input loop for college names
        while True:
            college = input("Type the college name or press 00 to confirm: ")
            if college != "00":  # Add college to list if not '00'
                l.append(college)
                print(f"Your current college list is {l}")
            else:  # Exit loop if '00' is entered
                break

        x = 0

        # Loop to collect ratings for each college
        while len(l) > x:
            campus_rating = int(input(f"Rate campus of {l[x]} (out of 10): ")) / 2  # Campus rating out of 5
            placements_rating = int(input(f"Rate placements of {l[x]} (out of 10): "))  # Placements rating out of 10
            crowd_rating = int(input(f"Rate crowd of {l[x]} (out of 10): ")) / 2  # Crowd rating out of 5
            
            # Total rating for the college
            college_ratings.append(placements_rating + campus_rating + crowd_rating)
            
            college_ranking.append(f"Points- {college_ratings[x]}, college- {l[x]}")
            
            x += 1

        # Sort colleges by ranking points
        college_ranking.sort(reverse=True)

        # Print out the ranked list
        y = 0
        while len(l) > y:
            print(f"Rank {y + 1}, {college_ranking[y]}")
            y += 1

def split_sort():
    #by Shardul Funde
    # Split Sort algorithm
    # Split Sort is a sorting algorithm that sorts a list of integers in ascending order
    # by splitting the list into two parts, sorting the parts separately, and then merging them back together.
    # The algorithm is implemented using a while loop and if-else statements.

    # Input list of integers to be sorted
    l = list(map(int, input("Enter integers separated by space: ").split()))
    y = []

    i = 0
    while i < len(l) - 1:
        if(l[i] > l[i + 1]):
            y.append(l[i + 1])
            l.pop(i + 1) 
        else:
            i += 1

    sorted_list = []

    sorted_list = l.copy()
    i = 0

    while i < len(y):

        for c in range(len(sorted_list)):
            if(y[i] <= sorted_list[c]):
                sorted_list.insert(c, y[i])
                break

        i += 1

    print(sorted_list)


def main():
    while True:
        print("\n--- OpenAlgos Algo library level 1---")
        print("Select an algorithm to run:")
        print("1. Thinking Calculator")
        print("2. College Ranker")
        print("3. Split Sort")
        print("4. Exit")
        
        user_choice = int(input("Enter your choice (Serial number of choice): "))
        
        if(user_choice == 1):
            solve_quadratic()
            
        elif(user_choice == 2):
            college_ranker()
            
        elif(user_choice == 3):
            split_sort()
        
        elif(user_choice == 4):
            print("Thank you for using OpenAlgos algorithm library level 1")
            break 
        
            
        
            
        else:
            print("Please enter valid number")
            continue
        
main()