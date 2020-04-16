file = input()

try:
    f = open(file)
except FileNotFoundError:
    print("File doesn't exsist")
except IOError:
    print("Input-output error")
except PermissionError:
    print("You haven't enought rights")
else:
    for line in f:
        print(line, end="")
