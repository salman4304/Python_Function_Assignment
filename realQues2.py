#  Create a function to generate a random password of given 
# length, containing uppercase, lowercase, numbers, and special characters.
def pass_val(psw):
        uppercount=lowercount=digits=specialcount=0
        for chr in psw:
            if chr.isupper():
                uppercount=uppercount+1
            elif chr.islower():
                lowercount=lowercount+1
            elif chr.isdigit():
                digits=digits+1
            else:
                specialcount=specialcount+1
        if uppercount>0 and lowercount>0 and digits>0 and specialcount>0:
                return psw
        else:
                msg="Invalid Password"
                return msg
            
length=8
password=input("Please Enter Password")
if len(password)<length:
    print("Invalid Password Length")
else:
     print("Your password is",pass_val(password))        