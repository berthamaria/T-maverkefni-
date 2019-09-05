#get an integer as an input.
#declair max_int to 0
#next we track if the input is a nagetive number
# if the input is a negative number the loop will end. /
# if negative number is enterd the highest input will be printed out.
#then we compare the value of the input to the max_int /
# and we will print out the maximum positive integer.

number = int(input('Enter an integer input: '))

max_num = 0

while number > 0:
    if number > max_num:
        max_num = number
    number = int(input('Enter an integer input: '))
print(max_num)