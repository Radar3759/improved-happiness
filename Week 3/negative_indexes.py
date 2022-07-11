#negative slicing starts at -1 from the last character and counts toward the first character
#I liked this explanation and based my code on their examples https://prepinsta.com/python/slicing-with-negative-numbers/


string = "Potato Salad"
#starts from the -8 to last character "t" and prints to, but doesn't include the -2 to the end character "a"
arr = string[-8:-2]
#prints string "to Sal"
print(arr)
