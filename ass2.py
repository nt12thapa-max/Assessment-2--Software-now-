limit = int(input("Enter any number up to 100: "))

prime = []

# prime number from 2 to limit
for num in range(2, limit + 1):
    is_prime = True

   # check if divisible
    for I in range(2, int(num ** 0.5) + 1):
       if num % I == 0:
          is_prime = False
          break
        
    #add to list if prime
    if is_prime:
        prime.append(num)

#Display result
print("prime numbers:", *prime)
print("total counts:", len(prime))

if prime:
    print("smallest numbers:", prime[0])
    print("largest numbers:", prime[-1])
    print("sum of primes:", sum(prime))
else:
    print("No numbers found.")