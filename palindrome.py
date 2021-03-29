i=int(input("enter the value:"))
rev=0
x=i
while (0<i):
	rev=(rev*10)+i%10
	i=i//10	
if (x==rev):
	print("palindrome number")
else:
	print("not palindrome number")
