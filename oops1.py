class student:
	cname='gpk'

	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
		
	def display (self):
		print('my name is',self.name)
		print('my rollno is',self.rollno)
	@classmethod
	def getcollagename(cls):
		print('collage name is',cls.cname)
	
	@staticmethod
	def average(x,y):
		print('average ',(x+y)/2)
			 
			 	 	 
s=student('durga',100)
s1=student('shubham',244)
s2=student('vaibhav',677)

s.display()
student.getcollagename()
student.average(10,20)













