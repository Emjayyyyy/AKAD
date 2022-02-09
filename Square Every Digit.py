#-----DETAILS-----
#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

#-----SOLUTION------

def square_digits(num):
    total_str = ''
    for element in str(num):
        square = int(element) ** 2
        total_str += str(square)
        
    return int(total_str)    