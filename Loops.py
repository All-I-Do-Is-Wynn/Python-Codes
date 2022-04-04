#All prime numbers <100
i=2
while(i<1000):
    j=2
    while(j <= (i/j)):
        if not(i%j): break
        j = j+1
    if (j > i/j): print (i, " is prime")
    i = i+1
print("All done")