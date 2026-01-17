import math

def calculate_math():
    try:
        number = float(input("Enter number: "))
        if number <=0:
            print("Please enter a positive number")
            return
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)

        print(f"Square root of {number} : {square_root}")
        print(f"Natural log of {number} : {natural_log}")
        print(f"Sin of {number} : {sine_value}")
    except ValueError:
        print(f"Invalid input. Please enter a valid number")

if __name__ == "__main__":
    calculate_math()


