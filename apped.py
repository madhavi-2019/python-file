file1 = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(file1 + "\n")

adt = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(adt + "\n")

with open("output.txt", "r") as file:
    content = file.read()
    print("\nFinal content of output.txt:")
