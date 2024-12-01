# Greatest common divisor of two numbers
def GCD(num1,num2):
    smaller=min(num1,num2)
    for i in range(1,smaller+1):
        if num1%i == 0 and num2%i == 0:
            hcf=i
    return hcf
first_num=int(input("Enter First Number"))
second_num=int(input("Enter Second Number"))
print(f"GCD or HCF of {first_num} and {second_num} is",GCD(first_num,second_num))