filename = input("Enter a name of the file: ")

try:
    file = open(filename, 'r')
    content = file.read()
except FileNotFoundError:
    print("File was not found!")