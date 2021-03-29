import sys
class customer:
	bankname='IDBI Bank'
	def __init__(self,name,balance=0):
		self.name=name
		self.balance=balance
		
	def deposit (self,amt):
		self.balance=self.balance+amt
		print('After deposit the balance ',self.balance)
		
	def withdraw (self,amt):
		if amt>self.balance:
			print('INSUFFICENT FUNDS...plz deposit the balance')
			sys.exit()
		else :
			self.balance=self.balance-amt
			print('After withdraw the balance ',self.balance)
				
print('welcome to ',customer.bankname)
name=input('Enter name: ')	
c=customer(name)

while True:
	print('d-Deposit\nw-Withdraw\ne-Exit')
	option=input('choose your option  ')
	
	if option=='d' or option=='D':
		amt=float(input('Enter the amount to deposit '))
		c.deposit(amt)
		
	elif option=='w' or option=='W':
		amt=float(input('Enter the amount to withdraw '))
		c.withdraw(amt)
		
	elif  option=='e'  or option=='W':
		print('Thanks for Banking')
		sys.exit()		
	else:
		print('choose valid option ') 
		
				
						
										
			
			














































