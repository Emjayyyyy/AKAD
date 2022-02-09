#-----DETAILS-----
#Can you find the needle in the haystack?

#Write a function findNeedle() that takes an array full of junk but containing one "needle"

#After your function finds the needle it should return a message (as a string) that says:

#"found the needle at position " plus the index it found the needle, so:

#find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
#should return "found the needle at position 5" (in COBOL "found the needle at position 6")




#-----SOLUTION------

def find_needle(haystack):
    position = 0
    for i in haystack:
        position += 1
        if i == "needle":
            return "found the needle at position " + str(position - 1)