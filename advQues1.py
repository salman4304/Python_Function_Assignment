def power(base,power):
    mul=1
    for x in range(power):
        mul=mul*base
    return mul
print(power(2,4))