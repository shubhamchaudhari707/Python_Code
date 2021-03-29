n=18
i=1
print("number of guesses is limited to only 9 times: ")
while (i<=9):
	guess_number=int(input("guess the number : \n"))
	if guess_number <18:
		print("you enter less number please input greater number: \n")
	elif guess_number >18:
		print("you enter greater number please input less number: \n")
	else:
		print("you win.")
		print("numer of guesses to took to finish ",i)
		break
	print(9-i,'number of guesses to left')
	i=i+1
if (i>9):
	print("game over")
		
				
			