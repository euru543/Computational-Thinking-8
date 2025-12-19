Athlete_points = 0
Dancer_points = 0
Normal_points = 0

answer1 = input("Do you prefer A Playing sports, B dancing, or C sleeping?   ")
if answer1 == "A":
    Athlete_points += 1
elif answer1 == "B":
    Dancer_points += 1
elif answer1 == "C":
    Normal_points += 1

answer2 = input("Is your favorite thing A energy drinks, B listening to music, or C or working?   ")
if answer2 == "A":
    Athlete_points += 0
elif answer2 == "B":
    Dancer_points += 1
elif answer2 == "C":
    Normal_points += 0

answer3 = input("Would you rather A workout, B sing, or C swim?   ")
if answer3 == "A" or answer3 == "B":
    Athlete_points += 1
elif answer3 == "C":
    Dancer_points += 0
    Dancer_points += 0

answer4 = input("What do you enjoy more? A team competitions, B performing on stage, or C relaxing at home?   ")
if answer4 == "A":
    Athlete_points += 1
elif answer4 == "B":
    Dancer_points += 1
elif answer4 == "C":
    Normal_points += 1


answer5 = input("Which sounds most fun? A running drills, B learning choreography, or C watching shows?   ")
if answer5 == "A":
    Athlete_points += 1
elif answer5 == "B":
    Dancer_points += 1
elif answer5 == "C":
    Normal_points += 1


answer6 = input("Pick an activity: A lifting weights, B freestyle dancing, or C hanging out with friends?   ")
if answer6 == "A":
    Athlete_points += 1
elif answer6 == "B":
    Dancer_points += 1
elif answer6 == "C":
    Normal_points += 1


answer7 = input("Your ideal weekend is: A training or practice, B music and movement, or C resting and gaming?   ")
if answer7 == "A":
    Athlete_points += 1
elif answer7 == "B":
    Dancer_points += 1
elif answer7 == "C":
    Normal_points += 1
print(f"Your score is {Athlete_points} Athlete, {Dancer_points} Dancer, and {Normal_points} Normal")

