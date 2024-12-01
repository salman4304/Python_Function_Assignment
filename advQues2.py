def temp_conversion(temp,scale):
    if scale=="C":
        temp_F=(9/5*temp) + 32
        return temp_F
    else:
        temp_C= (temp-32)*5/9
        return temp_C
temp=int(input("Please Enter Temperature"))
scale=input("Please Enter Scale like F or C")
print(temp_conversion(temp,scale))