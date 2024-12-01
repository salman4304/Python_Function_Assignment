def factorial(num):
    if num<0:
        print("Invalid Number")
    elif num==0:
        return 1
    else:
        fact=1
    for i in range(num,0,-1):
        fact=i*fact
    return num*factorial(num-1)
print(factorial(3))