# Writing to my_notes.txt
with open("my_notes.txt", "w") as file:
    file.write("This is my new file of notes\n")
    file.write("Let's learn file handling!\n")
    file.write("First, let's write to a file.\n")

# Reading from my_notes.txt
with open("my_notes.txt", "r") as file:
    content = file.read()
    print(content)

print("Done reading the file")

# Handling missing file exception
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("\nFile not found. Please create the file first.")

# Writing to story.txt
with open("story.txt", "w") as file:
    file.write("This is my new file. Let's write to this file in order to read and count the number of words in it.")

# Reading and counting words in story.txt
with open("story.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Total words:", len(words)) 

# Division with exception handling
try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    div = num1 / num2
    print("Division result:", div)

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Please enter a valid integer!")

# Writing a log entry and reading it correctly
with open("log.txt", "a") as file:
    file.write("New log entry!\n")

# Reading log file separately in "r" mode
with open("log.txt", "r") as file:
    content = file.read()
    print("Log File Content:\n", content)
