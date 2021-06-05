from .expense_report import prod_of_2020_sum, prod_of_2020_3_val_sum
import os
import sys


if __name__ == '__main__':

    try:
        star_step = int(sys.argv[1])
    except IndexError:
        raise Exception("Argument Required! Select 1 or 2.")
    except ValueError:
        raise Exception("Argument must be a number! Select 1 or 2.")

    with open(os.path.join(sys.path[0], "day01/input.txt"), "r") as file:
        expenses = [int(s) for s in file.readlines()]

        if star_step == 1:
            print(f"The sum is: {prod_of_2020_sum(expenses)}")
        elif star_step == 2:
            print(f"The sum is: {prod_of_2020_3_val_sum(expenses)}")
        else:
            raise Exception("Invalid Arguments: Select 1 or 2!")
