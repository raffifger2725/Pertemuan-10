word = input("Enter a word: ")
length = len (word)
num = 1
for x in word:
    position = length + num  
    letter = word [position]
    print (letter)
    num = num + 1