#Shivam kumar Roy
#20/10/2025
#Building a calorie tracking console app.

print("welcome to the daily calorie tracker")
print("This tool helps to track calories,meals and check you are in daily calorie limit or not")

#Input and Data Collection

Meals=["Breakfast","lunch","dinnner"]
calorie=[50,70,90]

num=int(input("How many meals do you want to enter:"))
for i in range(num):
    meal_name=input("Enter meal name:")
    meal_calorie=int(input("Enter meal calorie:"))
    Meals.append(meal_name)
    calorie.append(meal_calorie)
    print("meal successful")

#Calorie Calculations

calorie=sum(calorie)
average_calorie=calorie/num
daily_calorie_limit=int(input("enter the daily calorie limit:"))
print("total calorie:",calorie)
print("average calorie:",average_calorie)

#Exceed warning system

if calorie>daily_calorie_limit:
    print("warning")
else:
    print("You are within your daily calorie limit")

#Neatly formated output

print("your daily calorie report")
print("------------------------")
print("meal name\tcalorie")
print("------------------------")

for i in range(len(Meals)):
    print(f"{Meals[i]}\t\t{calorie}")

print("------------------------")
print(f"total:\t\t{calorie}")
print(f"average:\t{average_calorie:.2f}")