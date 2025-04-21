
# Check if prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            return False
    return True

# Print primes
def print_primes(num):
    for num in range(num):
        if is_prime(num):
            print(num, end=" ")
    print()
    
# Get primes
def get_primes(num):
    primes = []
    for num in range(num):
        if is_prime(num):
            primes.append(num)
    return primes