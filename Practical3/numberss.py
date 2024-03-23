"""The file has been renamed \"numberss"\ to not overright a module with the same name"""

#Importing the library math 
import math

#Ask the user to enter three different integers
list_num= input("Please enter 3 numbers spaced with a \"space\": ").split(" ")

# Converting to floats, then to integers in case someone put a decimal
list_castnum = [int(float(number)) for number in list_num]
print(list_castnum)
#or we could have trunked each item from their decimal parts
list_trunk= [math.trunc(float(number)) for number in list_num]
print(list_trunk)

#Print out the sum of all the numbers
print(sum(list_castnum))

#The first number minus the second number
substraction = list_castnum[0] - list_castnum[1]
print(substraction)

#Print out the third number multiplied by the first number
multiplication = list_castnum[2] * list_castnum[0]
print(multiplication)

#Print out the sum of all three numbers divided by the third number
sum_all = sum(list_castnum[0:3])/(list_castnum[2])
print(sum_all)
