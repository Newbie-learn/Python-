amount = float(input("Enter the total amount of bill  : "))
people = int(input("Enter No of people to split the bill between : "))
tip = float(input("Enter the percentage of tip to be given : "))

bill = (amount/people) + (amount * (tip/100))/people

print("Bill per person is :",bill)