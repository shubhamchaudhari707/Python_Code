class student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
		
	def display(self):
		print('hi',self.name)
		print('your marks is ',self.marks)
	
	def grade (self):
		if self.marks>=60:
			print('first class ')
		elif self.marks>50:
			print('second class')
		elif self.marks>35:
			print('third class ')
		elif self.marks>0:
			print('you got fail ')
		else:
			print('input valid keys')
			
n=int(input('enter numbers of students '))
for i in range(n):
	name=input('enter your name ')
	marks=int(input('enter your marks '))
	
	s=student(name,marks)
	s.display()
	s.grade()
	print('*'*20)



























