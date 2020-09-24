from fib import FibRealisations

if __name__ == "__main__":
    nums = [5, 1000, int((10**5)/2), 10**5, int((10**6)/2)]   

    for num in nums:
        fib = FibRealisations(num)
        print("Number of fib: {}".format(fib.n))
        fib.fib_v1()
        fib.fib_v2()
