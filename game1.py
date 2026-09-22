import random
Choices = ["rock","paper","scissors"]

user = input("Enter rock, paper or scissor: ")
computer = random.choice(Choices)

print("your chose:",user)
print("computer chose:",computer)

if user == computer:
    print("it' a Tie!")
elif ((user == "rock" and computer == "scissors") or 
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper")):
     print("You Win")
else :
     print("YOU LOST!")
     