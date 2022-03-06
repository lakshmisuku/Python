str=input("Enter the string : ")
print("Original string : ",str)
char=str[0]
length=len(str)
print("Length : ",length)
str=str.replace(char,'$')
str=char+str[1: ]
print("Replaced string : ",str)
