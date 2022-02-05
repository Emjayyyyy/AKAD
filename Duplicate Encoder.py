#-----DETAILS-----
#Given an array of integers, return a new array with each value doubled.

#For example:

#[1, 2, 3] --> [2, 4, 6]


#-----SOLUTION------


def duplicate_encode(word):
    word = word.lower()
    count = 0
    return_string  = ""
    for element in word:
        if word.count(element) > 1:
            return_string += ")"
        else:
            return_string += "("
            
    return  return_string       
        