# Create a function that takes a list of integers and returns the sum of all even numbers.
def even_sum(all_integers):
    addition=0
    for y in range(len(all_integers)):
        if all_integers[y]%2==0:
            addition=addition+all_integers[y]
    return addition
integers=[]
no_integers=int(input("How many integers do you want to enter"))
for x in range(no_integers):
    integer=int(input("Please Enter Integer"))
    integers.append(integer)
print("Sum of Even Integers:",even_sum(integers))