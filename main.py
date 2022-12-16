#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip calculator")
Bill=float(input("what is your total bill?$"))
Percentage=input("What percentage tip would you like to give ? 10, 12, 20?")
People=input("How many people to split the bill?")
result=int(Bill) + int(Bill)*float(int(Percentage) / int(100))
Tip=float(result) / float(People)
Tip2=round(Tip, 2)
print(f"Each person should pay :${Tip2}")