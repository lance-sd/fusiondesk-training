#Block A
name = input("What is your name?: ")
age = int(input("How old are you? "))
turn_100 = 2026 + (100 - age )

print(f"Hi {name}, if you are {age} years old, that means you will turn 100 years old in the year {turn_100}")

#Block B
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)



#Block C
def safe_divide(a, b):

    try:
       answer = a / b
       return answer
    except ZeroDivisionError:
        print("You unfortunately cannot divide by zero")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))


#Block D
people = [{"name": "Lance", "score": 85}, {"name": "Sipho", "score": 72}, {"name": "Zanele", "score": 91}] 

def highest_score(people):
    highest_so_far = 0
    name_highest = " "
    for person in people:
        if person["score"] > highest_so_far:
            highest_so_far = person["score"]
            name_highest = person["name"]
    return name_highest

print(highest_score(people))


#block E
 class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance = amount + self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            print("Withdrawal amount cannnot exceed balance, please try again")
            return None
        else:
            self.balance = self.balance - amount


        
    

























