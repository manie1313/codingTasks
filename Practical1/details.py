""" 
We will do 4 input functions to get the following information 
Name
Age
House number
Street 
"""
#Here, we can put all the information in a same line or do it separetely by declaring all the variable
# at once since the very beginning.(Unfortunately it seems we can't do multiple lines to have a ease
# the code reading, or maybe I just didn't search enough)
name, age, house_number, street = input(f"""Please enter your name, age, house number and street separated with a comma for each:""").split(",")

#Now we want to print the details the interface collected by breaking it into new lines
#thanks to the command \n
#print(f"Name: {name}\n Age: {age}\n House number: {house_number}\n Street: {street}")

#Let's print a proper sentence 
print(f"{name.capitalize()} is{age} and live in{house_number}, {street}street")