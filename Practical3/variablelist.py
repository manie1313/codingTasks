
# Python3 code to demonstrate 
# to assign variables from list element
# using list comprehension 
 
# initializing list  
test_list = [1, 4, 5, 6, 7, 3]
 
# printing original list
print ("The original list is : " + str(test_list))
 
# using list comprehension
# to assign variables from list element
var1, var2, var3 = [test_list[i] for i in (1, 3, 5)]
 
# printing result
print ("The variables are : " +  str(var1) +
                           " " + str(var2) +
                            " " + str(var3))
