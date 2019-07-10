import datetime

from random_num_gen import RandomNumGen

import numpy as np

import pandas as pd

d = datetime.datetime.today()
d = str(d)
d = d.replace(':', '-')


print("[1] Enter a number\n[2] Generate a number\n")

choice = int(input("Your Choice: "))

num_list = []
more_than_four = []

if choice == 1:
    num_list.append(input('Enter a number: \n'))

if choice == 2:
    amount = int(input("Enter how many numbers to generate and try: \n"))
    r = RandomNumGen()
    num_list = r.gen(amount)

for x in num_list:
    original_number = x
    counter = 0
    print('TESTING: ', x)
    while len(str(x)) != 1:

        new_num = 1
        int(new_num)
        counter += 1

        for digit in str(x):
            x = int(digit)
            new_num = new_num * x

        x = new_num
        print('New number: ', x)

    if counter > 3:
        vector = [original_number, counter]
        more_than_four.append(vector)
    print("Number of Iterations: ", counter, '\n')

print("These numbers have more than 4")
print('Date: ' + str(d))
print('List of lists: \n')
print(more_than_four)

ndArr = np.array(more_than_four)
print('2d Array: ')
print(ndArr)

dataframe = pd.DataFrame(data=ndArr)
print(dataframe)
dataframe.to_csv(path_or_buf='C:/Users/billy/Documents/GitHub/digit-multiply/data/' + d + '.csv')
