with open("original.txt", "r") as file:
    content = file.read()

modified_content = content.upper()

with open("modified.txt", "w") as new_file:
    new_file.write(modified_content)

print("File has been read and modified successfully!")
