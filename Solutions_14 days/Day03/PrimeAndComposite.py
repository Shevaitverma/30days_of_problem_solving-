def solve(num):

    def factorize(n):
        factors = []
        for i in range(1, n+1):
            if n%i == 0:
                factors.append(i)
        # print(F"Factors of {n} = {factors}")
        return factors

    def isPrime(n):
        if n==1:
            return False
        # check for 2 and 3
        if n<=3:
            return True # 2,3 are primes

        PrimeOrNot = True
        for i in range(2, n-1):
            if n%i == 0:
                PrimeOrNot = False

        if PrimeOrNot:
            return True
        else:
            return False

    prime = []
    composite = []
    for i in range(2, num+1):
        #print(F"Number to check is = {i}")
        if isPrime(i):
            prime.append(i)
        else:
            composite.append(i)

    print(f"Prime numbers = ", prime)
    print(f"composite numbers = ", composite)
    # for finding factors of compisite number 
    comp_dict = {}
    for i in composite:
        print(f"factors of {i}: ", factorize(i))
        
        
    

solve(10)