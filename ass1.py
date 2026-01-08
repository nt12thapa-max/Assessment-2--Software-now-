Limit = int(input("Enter any number up to 100: "))
                  
Prime= []

# prime number from 2 to limit
for num in range(2, limit + 1):
    is_prime = True
    
#program to check if any number is divided by any number from 2 to sqrt.
for I in range(2, int(num ** 0.5)+1):
        if num % I == 0:
            Is_prime = False
            break
    
 # Add number to list if it's prime
        if Is_prime:
         Prime.append(num)
  
 #Display result

print ("prime numbers:", *Prime)
print ("total counts:", len(Prime)) 

if Prime:
   print ("smallest numbers:", Prime [0])
   print ("largest numbers:", Prime [-1])
   print ("sum of primes:", sum (Prime))

else:
     print ("No numbers found.")

