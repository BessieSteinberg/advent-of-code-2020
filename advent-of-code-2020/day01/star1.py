from .expense_report import prod_of_2020_sum
import os
import sys

if __name__ == '__main__':

    with open(os.path.join(sys.path[0], "day01/input.txt"), "r") as file:
        expenses = [int(s) for s in  file.readlines()]

        print(f"The sum is: {prod_of_2020_sum(expenses)}")
