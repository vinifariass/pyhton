try:
    file = open("simple.txt", "r")
    if file.name == "simple.txt":
        raise IOError("File name is simple.txt")
    else:
        print(file.read())  # read the fileq
except IOError:
    print("Error: Could not read file")
finally:
    file.close()
