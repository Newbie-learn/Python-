import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input('''Enter your Choice : 
0 for Rock
1 for Paper
2 for Scissors
'''))

if user_choice == 0:
    print("You choose Rock")
    print(game_images[0])
elif user_choice == 1:
    print("You choose Paper")
    print(game_images[1])
elif user_choice == 2:
    print("You choose Scissors")
    print(game_images[2])
else:
    print("Wrong Input")


def concept():
    if computer_choice == user_choice:
        print("Its a draw")
    elif (user_choice == 0 and computer_choice == 1):
        print("Computer Won")
    elif (user_choice == 0 and computer_choice == 2):
        print("You Won")
    elif (user_choice == 1 and computer_choice == 2):
        print("Computer Won")
    elif (user_choice == 1 and computer_choice == 0):
        print("You Won")
    elif (user_choice == 2 and computer_choice == 0):
        print("Computer Won")
    elif (user_choice == 2 and computer_choice == 1):
        print("You Won")


if user_choice == 0 or user_choice == 1 or user_choice == 2:
    computer_choice = random.randint(0, 2)
    print("Computer Choose : " + str(computer_choice))
    print(game_images[computer_choice])
    concept()
else:
    pass





