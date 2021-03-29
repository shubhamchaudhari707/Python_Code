i=int(input("enter the value:"))
sum=0
prod=1
while (i>0):
	d=i%10
	if d%2==0:
		sum=sum+d
	else:
		prod=prod*i%10
		
	i=i//10
print("sum of digits =",sum, "prod of digits =",prod)
	







