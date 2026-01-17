def write_and_append():
    try:
        write_input = input("Enter to write to the file: ")
        with open("output.txt", "w") as file:
            file.write(write_input + "\n")
            print(f"Data added successfully to output.txt")
            print()

        append_input = input("Enter additional text to output: ")
        with open("output.txt", "a") as file:
            file.write(append_input + "\n")
            print(f"Data appended successfully to output.txt")
            print()

            print("Final content of data in output.txt file")
        with open("output.txt", "r") as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    write_and_append()