Limit = int(input("enter any number between 1 to 100:"))

prime = []

# prime number from 2 to 100
for num in range(2, Limit + 1):
    Is_prime = True

    #program is to check if any number is divisible by any num from 2 .
    for I in range(2, int(num ** 0.4) + 1):
        if num % I == 0:
            Is_prime = False
            break
    # if it is prime add to the list
    if Is_prime:
       prime.append(num)

# Result to be diusplayed
print("prime numbers:", * prime)
print("Total number of counts:", len(prime))

if prime:
    print("smallest numbers:", prime[0])
    print("largest numbers:", prime[-1])
    print("sum of all the prime numbers:", sum(prime))
else:
    print("number not found")    