
def greet():
    print("Hi all")
    print("Welcome to Revit API Training")
    print("This is C# Programming")
    print("Hope you all are not asleep!!!")

def subtract(a, b):
    print(a - b)

def sumOfAllNumbers(*inputs):
    total = 0
    for n in inputs:
        total += n
    print(total)

# CALL FUNCTIONS
greet()
subtract(10, 5)
sumOfAllNumbers(1, 2, 3, 4)              