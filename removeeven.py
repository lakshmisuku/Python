num1=input("Enter an integer : ")
num=list(map(int,num1.split()))
num=[x for x in num if x%2!=0]
print("List after removing even numbers ",end=' ')
print(num)
