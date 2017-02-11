def Fizzbuzz(n):
    # Initialize f array with first two values 0 and 1 to length n
    f = [0] * (n)
    f[0] = 0
    f[1] = 1

    # Loop over n numbers
    for i in range(n):
        # Print first two numbers no matter what
        if i <= 1:
            print("%d" % f[i])
        else:
            f[i] = f[i - 1] + f[i - 2]
            prime = is_prime(f[i])      # Check primality of number
            if prime:
                print("BuzzFizz")
            elif (f[i] % 15) == 0:      # Check divisibility by 15
                print("FizzBuzz")       # Note: Can combine next two statements for 15 check, this code is cleaner IMO.
            elif (f[i] % 5) == 0:       # Check divisibility by 5
                print("Fizz")
            elif (f[i] % 3) == 0:       # Check divisibility by 3
                print("Buzz")
            else:                       # Any other case print the number in the sequence
                print("%d" % f[i])

    return 'End of Sequence'


def is_prime(n):
    # No primes 1 or less by def
    if n <= 1:
        return False
    elif n <= 3:                    # 2,3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:  # Divisible by 2 or 3 is not prime
        return False

    i = 5                           # Check if divisible by 5, 7, 11, etc
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
