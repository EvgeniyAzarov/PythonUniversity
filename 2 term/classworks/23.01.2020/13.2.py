def listOfNumbers(file):
    nums = []
    f = open(file)
    for line in f:
        nums += map(float, line.split())
    f.close()
    return nums

def sum(nums):
    s = 0
    for n in nums:
        s += n
    return s

def countNegatives(nums):
   c = 0
   for n in nums:
       if n < 0: 
           c += 1
    return c

def lastNumber(nums):
    return nums[-1]

def maxNumber(nums):
    m = -inf
    for n in nums:
        if n > m:
            m = n
    return m

def maxOnEven(nums):
    m = -inf
    for i in range(0, len(nums), 2):
        if nums[i] > m:
            m = nums[i]
    return m

file = "homeworks/13. Файлы/numbers.txt"

