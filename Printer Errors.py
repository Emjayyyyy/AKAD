#-----DETAILS-----

#Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

#You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

#The string has a length greater or equal to one and contains only letters from ato z.

#Examples:
#s="aaabbbbhaijjjm"
#printer_error(s) => "0/14"

#s="aaaxbbbbyyhwawiwjjjwwm"
#printer_error(s) => "8/22"


#-----SOLUTION------
def printer_error(s):
    
    count  = 0
    a_ascii = ord("a")
    m_ascii = ord('m')
    
    
    valid_ascii_list = range(a_ascii,(m_ascii+1))
    
    s_list = [elem for elem in s]
    
    for element in s_list:
        if ord(element) in valid_ascii_list:
            continue
        else:
            count += 1;
            
    return "{}/{}".format(str(count),str(len(s)))        