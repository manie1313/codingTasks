#Write Python code to take the name of a user's favourite restaurant and
#store it in a variable called string_fav.

string_fav = str(input(f"Could you tell us what's your favorite restaurant?: "))

#Below this, write a statement to take in the user's favourite number. Use
#casting to store it in an integer variable called int_fav.

int_fav = int(input("Could you tell us what's your favorite number?: "))

#Print out both of these using two separate print statements below what
#you have written. Be careful!

print({string_fav})
print({int_fav})

#Once this is working, try to cast string_fav to an integer. What happens?
#Add a comment in your code to explain why this is.

cast_stringtoint = int(string_fav)
print(cast_stringtoint)

""" A ValueError appears: ValueError: invalid literal for int() with base 10: 'jijoo'
Because it's not possible to change strings into integers """



