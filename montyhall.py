import random 
n = 0 
orig = 0 
swi = 0
while(n <= 3):
	car = random.randint(1,3)
	door1 = car 
	door2 = car 
	user = int(input("Choose a number between 1 and 3.\n"))
	rev = car
	while(rev == car or rev == user):
		rev = random.randint(1,3)
	print("A goat is behind door", rev)
	ch = int(input("Enter your final choice.\n"))
	if(ch == user and user == car):
		print("You won through your original choice.")
		orig += 1 
	elif(ch != user and ch == car):
		print("You won by switching!")
		swi += 1
	elif(ch == user and user != car):
		print("You could've won by switching!")
		swi += 1 
	elif(ch != user and user == car):
		orig += 1 
		print("You could've won by staying!")
	print("Car was behind door", car)

	n += 1 

swip = (swi/n)*100
origp = (orig/n)*100

print("Percentage win by switching is:",swip)
print("Percentage win by staying is:", origp)
