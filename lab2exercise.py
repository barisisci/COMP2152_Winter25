import random

choices = ["Rock","Paper","Scissors"]
playerChoices = str(input(">")).capitalize()
if playerChoices not in choices:
    raise ValueError("Invalid choice! Please enter 'Rock','Paper','Scissors'")
computerChoices = random.randint(0,2)


print(f"Player choose {playerChoices}!")
print(f"Computer choose {choices[computerChoices]}!")


if playerChoices == choices[computerChoices]:
    print("It's a tie")
    print("Looks like we're evenly matched.")

elif playerChoices == "Rock" and choices[computerChoices] == "Scissors":
    print("Player wins!")
    print("You got lucky this time!")
elif playerChoices == "Scissors" and choices[computerChoices] == "Rock":
    print("Computer wins!")
    print("Better luck next time!")
elif playerChoices == "Paper" and choices[computerChoices] == "Scissors":
    print("Computer wins!")
    print("Better luck next time!")
elif playerChoices == "Paper" and choices[computerChoices] == "Rock":
    print("Player wins!")    
    print("You got lucky this time!")
elif playerChoices == "Rock" and choices[computerChoices] == "Paper":
    print("Computer wins!") 
    print("Better luck next time!")
elif playerChoices == "Scissors" and choices[computerChoices] == "Paper":
    print("Player wins!")    
    print("You got lucky this time!")
 