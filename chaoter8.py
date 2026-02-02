# a = 12
# b = 45
# c = 56

# average = (a+b+c)/3
# print(average)


# This is a defination of function
# def avg():
#     a = int(input("Enter your number"))
#     b = int(input("Enter your number"))
#     c = int(input("Enter your number"))

#     average = (a+b+c)/3
#     print(average)

# this is a funcyion call
# avg()
# print("Thanku")
# avg()
# print("Thanku")
# avg()
# print("Thanku")
# avg()
# print("Thanku")
# avg()
# print("Thanku")
# avg()



# quickquiz

# def goodday():
#     a = (input("Enter your name:-"))
   
#     print("good day",a)

# goodday()


# function with arguments name and ending are perimeter
# def goodday(name, ending):
#     print("good day," + name)
#     print(ending)
#     return "Done"

# a = goodday("Hsrry", "Thank you")
# print(a)

# goodday("Shivam", "Thank you")
# goodday("Sakshi", "Thanks")



# defoult parameter valu
# def goodday(name,ending="Thanku"):
#     print(f"good day {name}")
#     print(ending)

# goodday("Harry","Thanks")
# goodday("Shivam")




#                              Recursion

# def factroial(n):
#     if(n==1 or n==0):
#         return 1
#     return n* factroial(n-1)

# n = int(input("Enter a number"))
# print(f"The fsctroil of a number is:- {factroial(n)}")




#                         practice



# Q find greatest of two number

# def greatest(a,b,c):

#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#       return c

# a = 1
# b = 2
# c = 3

# print(greatest(a,b,c))

# Q using function to convert celceus to fornheight

# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter tempreture in F: "))
# c = f_to_c(f)
# print(f"{round(c,2)} C")

# question new line ko avoid kasa karogea as a print function

# print("a")
# print("b")
# print("c", end="")
# print("d" ,end="")

# Q write a recursive function to calculate a sum of n natural number

# def sum(n):
#     if(n==1):
#        return 1
#     return sum(n-1) + n

# print(sum(4))

# q star printing

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(3)

# Q convert inch to centimter

# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("Enter value in inches: "))

# print(f"The corresponding value in cm is {inch_to_cms(n)} ")

# Question

# def rem(l,word):
#     for item in l:
#       l.remove(word)
#       return l

# l = ["Shivam","Satyam","Sonu", "Rupak","ab"]

# print(rem(l,"ab"))


# def rem(l,word):
#     n = []
#     for item in l:
#        if not(item == word):
#           n.append(item.strip(word))
#     return n

# l = ["Shivam","Satyam","Sonu", "Rupak","ab"]

# print(rem(l,"ab"))

# Q write a multiply table of given number

# def multiply(n):
#     for i in range(1, 11):
#         print(f"{n}*{i} = {n*i}")

# multiply(5)

