def factorial(num):
    if num < 0 :
        return "Factorial is not defined for negative number"
    result = 1
    for i in range (1,num + 1):
        result *=i
    return  result

if __name__ == "__main__":
    number = int(input("Enter Number: "))
    print(f"Factorial of {number} is: {factorial(number)}")