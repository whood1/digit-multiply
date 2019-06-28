user_num = input('Enter a number: \n')

counter = 0

while len(str(user_num)) != 1:

	new_num = 1
	int(new_num)
	counter += 1
	

	for digit in str(user_num):
		x = int(digit)
		new_num = new_num * x


	user_num = new_num
	print('New number: ', user_num)


print("Number of Iterations: ", counter)