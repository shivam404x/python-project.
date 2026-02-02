for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


name = "Shivam"
age = 18
print("my name is %s and i am %d years old" % (name, age))


# str.format()

name = "Shivam"
age = 18
print("my name is {p} and i am {a} years old".format(p=name, a=age))


name = "Shivam"
age = 18
print(f"my name is {name} and i am {age} years old.")

# 4th question

b = 8000
while 1:  # infinte loop bnanea ke liya use hota hai
    c = input("1.Check 2.Withdraw 3.Deposit 4.Exit: ")
    if c == '1':
        print("Balance:", b)
    elif c == '2':
        a = int(input("Withdraw: "))
        b = b-a if a <= b else print("No balance!")
    elif c == '3':
        b += int(input("Deposit: "))
    elif c == '4':
        print("Bye!")
        break
    else:
        print("Invalid!")


# circle question

shape = input("Enter shape (circle/square/rectangle/triangle): ").lower()

if shape == "circle":
    r = float(input("Radius: "))
    print(f"Area={3.14*r*r}, Perimeter={2*3.14*r}")

elif shape == "square":
    a = float(input("Side: "))
    print(f"Area={a*a}, Perimeter={4*a}")

elif shape == "rectangle":
    l = float(input("Length: "))
    w = float(input("Width: "))
    print(f"Area={l*w}, Perimeter={2*(l+w)}")

elif shape == "triangle":
    b = float(input("Base: "))
    h = float(input("Height: "))
    s1 = float(input("Side1: "))
    s2 = float(input("Side2: "))
    print(f"Area={0.5*b*h}, Perimeter={b+s1+s2}")

else:
    print("Invalid shape")


class A:
    def_int_(self):
    print("a constructer")


class B(A):
    def_int(self)
    print("b contruc")


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity = seating_capacity

    def display_info(self):
        super().display_info()
        print("Seating Capacity:", self.seating_capacity)


class ElectricCar(Car):
    def __init__(self, brand, model, seating_capacity, battery_range):
        super().__init__(brand, model, seating_capacity)
        self.battery_range = battery_range

    def display_info(self):
        super().display_info()
        print("Battery Range:", self.battery_range, "km")


e1 = ElectricCar("Tata", "Model S", 5, 600)
e1.display_info()
