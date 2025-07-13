#Problem: 01

#Write a function that takes two numbers as input and returns their average. Call the function with different values.

def call_avg(num1, num2):
    average = (num1 + num2) / 2
    return average

t = int(input("Enter how many times you want to call function: "))

for i in range(t):
    num1, num2 = map(int, input(f"Enter two numbers: ").split())
    print("Average:", call_avg(num1, num2))