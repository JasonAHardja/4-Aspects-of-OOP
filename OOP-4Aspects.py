#Encapsulation
class Car:
    def __init__(self, make, model, year):
        self.__make = make  #Using double underscores for private attribute
        self.__model = model
        self.__year = year
        self.__mileage = 0

    #Getter methods to access private attributes
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    #Setter method to modify private attribute
    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            print("Mileage cannot be negative.")

    #Method to drive the car
    def drive(self, miles):
        if miles > 0:
            self.__mileage += miles
            print(f"Car has been driven {miles} miles.")
        else:
            print("Invalid mileage value.")

#Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

#Access attributes using getter methods
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())
print("Mileage:", my_car.get_mileage())

#Use setter method to modify mileage
my_car.set_mileage(1000)

#Drive the car
my_car.drive(100)

#Check updated mileage
print("Updated Mileage:", my_car.get_mileage())





#Polymorphism - Method Overridding
class Circle:
    def shape(self):
        print("Shape is Circle")

class Square:
    def shape(self):
        print("Shape is Square")
        
class Triangle:
    def shape(self):
        print("Shape is Triangle")
 

#subclass
circle = Circle()
square = Square()
triangle = Triangle()


#overriding the method
circle.shape()
square.shape()
triangle.shape()




#Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

#Derived class
class Man(Person):
    def __init__(self, name, age, beard_length):
        #Call the constructor of the base class
        super().__init__(name, age)
        self.beard_length = beard_length

    def display_info(self):
        #Override the display_info method of the base class
        return f"Man - {super().display_info()}, Beard Length: {self.beard_length} inches"

# Derived class 
class Woman(Person):
    def __init__(self, name, age, hair_length):
        #Call the constructor of the base class
        super().__init__(name, age)
        self.hair_length = hair_length

    def display_info(self):
        #Override the display_info method of the base class
        return f"Woman - {super().display_info()}, Hair Length: {self.hair_length} inches"

#Create instances of the derived classes
man = Man("Man", 30, 1.5)
woman = Woman("Woman", 25, 12)

# ¥Call methods of the base and derived classes
print(man.display_info())
print(woman.display_info())




#Abstraction
from abc import ABC, abstractmethod

#Abstract base class using the ABC module
class Account(ABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_info(self):
        pass

#Concrete class implementing the Account abstract class
class SavingsAccount(Account):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def display_info(self):
        print(f"Savings Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate}")
        print(f"Calculated Interest: {self.calculate_interest()}")

#Concrete class implementing the Account abstract class
class CheckingAccount(Account):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Transaction denied. Overdraft limit exceeded.")

    def display_info(self):
        print(f"Checking Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        print(f"Overdraft Limit: {self.overdraft_limit}")

#Example usage
savings_account = SavingsAccount("Banker1", 5000, 0.03)
checking_account = CheckingAccount("Banker2", 2000, 1000)

savings_account.deposit(1000)
savings_account.withdraw(500)
savings_account.display_info()

print("\n")

checking_account.withdraw(2500)
checking_account.deposit(1200)
checking_account.display_info()
