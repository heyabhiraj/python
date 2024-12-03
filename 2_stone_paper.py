import random
gen=random.random()

print("Welcome to Stone, Paper and Scissor Game \nYou are playing this game with Computer \nLet's Play the Game...\n")
'''User Choice'''

#User Choice
user_choice=str(input("Choose Stone, Paper or Scissor: ")).lower()
if user_choice not in ["stone","paper","scissor"]:
    print("Invalid Choice, Please try again")
    exit()

#Computer Choice
if 0<=gen<0.3:
    computer_choice='stone'
    print(f"\nComputer's Choice is {computer_choice}\n")
elif 0.3<=gen<0.7:
    computer_choice='paper'
    print(f"\nComputer's Choice is {computer_choice}\n")
elif 0.7<=gen<=1:
    computer_choice='scissor'
    print(f"\nComputer's Choice is {computer_choice}\n")

print("Result:")
if user_choice==computer_choice:
    print("Oo, It's a tie!")
elif (user_choice == 'stone' and computer_choice == 'scissor') or \
     (user_choice == 'paper' and computer_choice == 'stone') or \
     (user_choice == 'scissor' and computer_choice == 'paper'):
    print("Congratulations!! You have won the Game.")
else:
    print("Sorry!! You lose the Game.")
