# def multiply(*nums):
#     a = 1
#     for n in nums:
#         a *= n
#         print(a)
# multiply(2,3,4)
# multiply(3,5,6,24)

# def person(**info):
#     name = info["name"]
#     age = info["age"]
#     print(f"Name: {name}")
#     print(f"age: {age}")

# person(name = "Shivam",age=20)

# Recoation

# def sum_n(n):
#     if n ==1 :
#         return 1
#     return n+sum_n(n-1)
# print(sum_n(5))

# program not run

# class Dog:
#     def int(self,Name)
#         self Name=Name
#     def display_name(self):
#         print(f/Dog nme:)

# class retriver:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print (f"{self.name} is barking!")
    
#     def details(self):
#         print (f"Name: {self.name}, Age: {self.age}")

# # Object banana
# dog = retriver("Tommy", 3)

# print(dog.details())
# print(dog.bark())

# a = input("Enter the value of a:")
# print(type(a))

# a = int(input("Enter your number 1:"))
# b = int(input("Enter your number 2:"))
# print("a is greater than b is " ,a>b)
# print("The average of two number is ",(a+b)/2)
# print("The swuare of two number is ",a**2)

# a = int(input("Enter a number"))
# b = int(input("Enter a nmber"))

# rer=a/b
# print("rer")

# class BankAccount:
#     def _init_(self, acc_no, name, balance=0):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#     # Deposit method
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} deposited successfully.")
#         else:
#             print("Invalid deposit amount.")

#     # Withdraw method
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         elif amount <= 0:
#             print("Invalid withdraw amount.")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdrawn successfully.")

#     # Display account information
#     def display(self):
#         print("\n--- Account Information ---")
#         print(f"Account Number : {self.acc_no}")
#         print(f"Name           : {self.name}")
#         print(f"Balance        : {self.balance}")
#         print("---------------------------")


# # --------- Demonstration with 3 accounts ---------

# a1 = BankAccount(101, "Rahul", 5000)
# a2 = BankAccount(102, "Aman", 3000)
# a3 = BankAccount(103, "Neha", 2000)

# # Transactions
# a1.deposit(1500)
# a1.withdraw(1000)

# a2.withdraw(500)
# a2.deposit(2000)

# a3.deposit(500)
# a3.withdraw(300)

# # Display details
# a1.display()
# a2.display()
# a3.display()



