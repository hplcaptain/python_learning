def read():
    try:
        with open("sample.txt", "r") as file:
            print(f"File Content: \n")
            for i in file:
                print(i.strip())
    except FileNotFoundError:
        print("Error: The Sample.txt file not found")
    except Exception as e:
        print(f"Error Occurred: {e}")

if __name__ == "__main__":
    read()
