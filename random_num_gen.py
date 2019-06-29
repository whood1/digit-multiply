import random

def generate_numbers(user_num):

	number = ''
	return_list = []
	for x in range(user_num):
		length = random.randint(1, 10)
		for y in range(length):
			r = random.randint(1,10)
			number = (str(number), str(r))
		return_list[x] = (number)
	return return_list


		

user_num = input('Enter the number of numbers youd like to try: \n')

user_num = int(user_num)

num_list = generate_numbers(user_num)

print(num_list)