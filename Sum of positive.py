#-----DETAILS-----

#You get an array of numbers, return the sum of all of the positives ones.

#Example [1,-4,7,12] => 1 + 7 + 12 = 20

#Note: if there is nothing to sum, the sum is default to 0.


#-----SOLUTION------
def positive_sum(arr):
    if len(arr) == 0: 
      return 0
    return sum([ele for ele in arr if ele > 0])
