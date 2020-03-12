s = input()
sum = 0
for c in s:
    try:
        sum += int(c)
    except ValueError: 
        pass

print(sum)
