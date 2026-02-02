# loops in python chapter 7

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)

# the same task can be done like this and this is a for loop

# for i in range(1,6):
#     print(i)

# know we are using a while a loop
 
# i = 1

# while(i<51):
#     print(i)
#     i +=1

# example print shivam 5 times

# i = 0
# while(i<5):
#     print("Shivam")
#     i = i+1 or i +=1 both are same thing

# printing of list content using while loop
# l = [ 1,"Shivam",False,"Rupak","Subedhar"]

# i = 0

# while(i<len(l)):
#     print(l[i])
#     i +=1

# for loop concept

# for i in range(7):
#     print(i)

#for loop with list
# l = [1,4,6,4354,5,4678,89]

# for i in l:
#     print(i)

#for loop with tuple
# t = (6,56,67,78)
# for i in t:
#     print(i)

#for loop with string
# s = "Shivam"
# for i in s:
#     print(i)

# problem with else

# l = [1,3,4,9]

# for item in l:
#     print(item)

# else:
#     print("done")


# break and continue
# for i in range(100):
#  if(i == 34):
#     break  #Exit the loop right now
# print(i)

# for i in range(100):
#  if(i == 34):
#     continue  # Skip this itration(value of i)
#  print(i)



# for i in range(456):
#     pass #it is a nul statement in python it in struct to do nothing



# i = 0
# while(i<67):
#     print(i)
#     i += 1

#                   now its time to practice👇
# Question print table of any number program
# n = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# Question grite a persion whose name is start wth s

# l = ["Shivam","Satyam","Sachin","Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# and question is solving with while loop

# n = int(input("Enter your number:-"))

# i = 1
# while(i<11):
#     print(f"{n} * {i} = {n * i}")
#     i += 1

# Question write a program to determine the number is prime or not

# n = int(input("Enter your number:-"))

# for i in range(2, n):
#     if(n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("number is prime")

# Question write a programm to sum a natural number using a whilw loop

# s = int(input("Enter your number:-"))

# i = 0
# sum = 0
# while(i<=s):
#     sum += i
#     i+=1
# print(sum)

# Question findindg a factorial  of number program

#5! = 1*2*3*4*5

# s = int(input("Enter your number:-"))
# product = 1
# for i in range(1, s+1):
#     product = product * i
# print(f"The factorial of {s} is {product}")

#               star pattern program

# question one

# n = int(input("Enter your number:-"))
# for i in range(1,n+1):
#   print(""*(n-i),end="")
#   print("*"* (2*i-1),end="")
#   print("")

# Question two

# n = int(input("Enter your number:-"))
# for i in range(1,n+1):
#   print("*" * i,end="")
#   print("")

# question three


# n = int(input("Enter your number:-"))
# for i in range(1,n+1):
#    if(i==1 or i==n):
#       print("*"* n,end="")
#    else:
#       print("*",end="")
#       print(" "*(n-2),end="")
#       print("*",end="")
#    print("")


# question four

# n = int(input("Enter your number:-"))

# for i in range(1,11):
#     print(f"{n}*{11-i} = {n*(11-i)}")
