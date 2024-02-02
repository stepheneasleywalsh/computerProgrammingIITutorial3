import os

# First let us check if primes.csv exists, we need to make it, if not
if not os.path.exists("primes.csv"):
    f = open("primes.csv","w")
    f.write("primes")
    f.close()
    print("Creating primes.csv file.")

def isPrime(n):
    # SLOW NAIVE SCHOOL METHOD (EASY BUT SLOW)
    numberOfFactors = 0
    # Checking how many factors n has
    for m in range(1,n+1):
        if n%m == 0: # This means m is a FACTOR of n so it CAN'T BE PRIME
            numberOfFactors += 1
    # Primes have 2 factors only
    if numberOfFactors == 2:
        return True
    else:
        return False

# Get the last entry from the file
last = ""
f = open("primes.csv","r")
for row in f:
    last = row
f.close()

# Open File
f = open("primes.csv","a")


# Check where I need to start
if last == "primes":
    n = 1
else:
    n = int(last)+1

# Generate Primes into CSV
numberOfPrimes = 0
while True:
    if isPrime(n):
        f.write("\n"+str(n))
        numberOfPrimes += 1

    if numberOfPrimes == 1000:
        break

    n += 1

# Done
f.close()
print("DONE")
quit()