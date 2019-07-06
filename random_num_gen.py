import random


class RandomNumGen:
    def __init__(self):
        self.x = 2

    # Generates list of random numbers
    def gen(self, amount):
        number_list = []

        # For the number of numbers we will generate
        for x in range(amount):
            number = random.choice(range(2, 100000000000000))
            number_list.append(number)

        return number_list

