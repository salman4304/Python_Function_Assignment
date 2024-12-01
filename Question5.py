def is_prime(num):
    if num>1:
        for x in range(2,num):
            if num%x==0:
                return False
                break
        else:
            return True
    return False
number=int(input("Please Enter Number"))
if is_prime(number)==True:
    print("Entered Number Is Prime")
else:
    print("Entered Number is not Prime")