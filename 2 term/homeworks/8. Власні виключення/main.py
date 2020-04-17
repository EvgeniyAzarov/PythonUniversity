from custom_set import CustomSet

cs = CustomSet()

cs.add('asdf')
cs.add('asdggsdf')
cs.add(3)
cs.add(4.34)
cs.add(7.983)
cs.add(6+8j)

for c in cs:
    print(c)

