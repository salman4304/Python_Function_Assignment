# Create a function that takes a list of numbers and returns the largest number.
def largest(all_numbers):
    largest_num=all_numbers[0]
    for num in all_numbers:
        if num>largest_num:
            largest_num=num
    return largest_num
numbers_list=[]
total=int(input("How many numbers do you want to enter"))
for x in range(total):
    number=int(input("Please Enter Number"))
    numbers_list.append(number)
print("Largest Integer is:",largest(numbers_list))