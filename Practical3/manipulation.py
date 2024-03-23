
str_manip = input("Please enter a sentence: ")
str_manipbis = str(str_manip.strip(" "))
#print(str_manipbis)

#the len function counts spaces as well
sentence_withspaces = len(str_manip)
print(sentence_withspaces)
#if we ever wanted to count without the spaces, we could join characters altogether
sentence_withoutspaces = str_manipbis.replace(" ", "")
sentence_withoutspacesbis = len(sentence_withoutspaces)
print(sentence_withoutspacesbis)

#Find the last letter in str_manip sentence. 
last_char = str_manipbis[-1]
print(str_manipbis[-1])
replace_sentence = str_manipbis.replace(last_char, "@")
print(replace_sentence)

#Print the last 3 characters in str_manip backwards.
print(str_manipbis[-1:-4:-1])

#Create a five-letter word that is made up of the first three characters
#and the last two characters in str_manip.
new_word = (str_manipbis[0:3:1])+(str_manipbis[-1:-3:-1])
print(new_word)




