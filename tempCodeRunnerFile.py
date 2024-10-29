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
