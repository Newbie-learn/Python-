print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Love Calculator Using Name

final_score = name1 + name2

lower_case_string = final_score.lower()

#TRUE LOVE COUNT
t = lower_case_string.count("t")
u = lower_case_string.count("r")
r = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if (love_score>90)  or (love_score < 10):
  print(f"Your Score is {love_score}, you go like coke and mentos.")
elif love_score>40 and love_score<50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")