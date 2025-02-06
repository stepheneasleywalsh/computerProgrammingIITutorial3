def isPrime(x): # Create a function to check if x > 1 is prime
    factors = 0
    for n in range(1,x+1):
        if x%n == 0:
            factors += 1
        if factors > 2:
            return False
    return True

try: # Open the file (if it exists)
    f = open("primes.csv","r")
    for line in f.readlines():     # I'm getting the LAST int in the file
        start = 1+(int(line.replace("\n","")))
    f.close()
except FileNotFoundError: # Create the file (if does not exist)
    f = open("primes.csv", "x")
    start = 2 # first prime
    f.close()

# Add to the file
x = start
want = 1000
make = 0
f = open("primes.csv","a") # APPEND (add) to the file
while make < 1000:
    if isPrime(x):
        if not x == 2:
            f.write("\n"+str(x))
        else:
            f.write(str(x))
        make += 1
    x += 1
f.close()
