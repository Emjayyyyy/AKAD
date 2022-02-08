#-----DETAILS-----
#Nathan loves cycling.

#Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

#You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

#For example:

#time = 3 ----> litres = 1

#time = 6.7---> litres = 3

#time = 11.8--> litres = 5Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


#-----SOLUTION------


def litres(time):
    return(time//2)