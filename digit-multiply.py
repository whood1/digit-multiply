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
    num_list.append(input('Enter a number: \n'))jg

    if counter > 0:
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
