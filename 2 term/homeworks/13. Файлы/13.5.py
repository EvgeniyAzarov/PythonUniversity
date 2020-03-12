import math

def read_numbers(file):
    nums = []
    with open(file) as f:
       for line in f:
           nums.extend(list(map(int, line.split())))
    return nums

def count_even(n):
    c = 0
    for i in n:
        if i % 2 == 0:
            c += 1
    return c

def count_odd_squares(n):
    c = 0
    for i in n:
        if (i**(1/2))**2 == i and i**(1/2) % 2 == 1:
            c += 1
    return c

def max_even_odd_diff(n):
    max_even = -math.inf
    min_odd = math.inf

    for i in n:
        if i % 2 == 0 and i > max_even:
            max_even = i
        elif i % 2 == 1 and i < min_odd:
            min_odd = i

    return max_even - min_odd

def longest_increase_subseq(n):
    d = [None for i in n]
    d[0] = 1
    for i in range(1, len(n)):
        p = [0]
        for j in range(i):
           if n[j] < n[i]:
               p.append(d[j])
        d[i] = max(p) + 1
    
    return max(d)

file = "numbers.txt"
n = read_numbers(file)

print(n)

print("a) ", count_even(n))
print("b) ", count_odd_squares(n))
print("c) ", max_even_odd_diff(n))
print("d) ", longest_increase_subseq(n))

