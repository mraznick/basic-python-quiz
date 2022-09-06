print("Welcome to my plant quiz!")

playing = input("Are you ready? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play ^_^")
score = 4

answer = input("What is the most common killer of houseplants? ")
if answer.lower() == "root rot":
    print("Bingo!")
else:
    print("Sorry, that's incorrect! You lose 1 point!")
    score -= 1


answer = input("In which month does the growing season begin in the US? ")
if answer.lower() == "march":
    print("Bingo!")
else:
    print("Sorry, that's incorrect! You lose 1 point!")
    score -= 1


answer = input("In which month does the growing season END in the US? ")
if answer.lower() == "october":
    print("Bingo!")
else:
    print("Sorry, that's incorrect! You lose 1 point!")
    score -= 1

answer = input(
    "True or False: It is possible to have too many houseplants... ")
if answer.lower() == "false":
    print("Bingo!")
else:
    print("Sorry, that's incorrect! You lose 1 point!")
    score -= 1

print("Your final score is " + str((score / 4) * 100) + "%! Great job!")
