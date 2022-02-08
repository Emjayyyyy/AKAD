#-----DETAILS-----
#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

#Examples
#"din"      =>  "((("
#"recede"   =>  "()()()"
#"Success"  =>  ")())())"
#"(( @"     =>  "))((" 

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
        