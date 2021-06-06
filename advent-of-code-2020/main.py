import argparse
import os
import sys
from day1.expense_report import prod_of_2020_sum, prod_of_2020_3_val_sum
from day2.password_validator import count_valid_passwords_policy_1, count_valid_passwords_policy_2
from day3.tree_navigator import count_trees_hit_delta_3


class InvalidArgument(Exception):
    pass


DAYS = {
    1: {
        'star_funcs': [prod_of_2020_sum, prod_of_2020_3_val_sum],
        'per_line_func': int
    },
    2: {
        'star_funcs': [count_valid_passwords_policy_1, count_valid_passwords_policy_2]
    },
    3: {
        'star_funcs': [count_trees_hit_delta_3]
    }
}


def get_day_and_star():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=int)
    parser.add_argument("-s", "--star", type=int)

    args = parser.parse_args()

    if args.day not in DAYS:
        raise InvalidArgument(f"{args.day} is not a valid choice for -d/--day")

    if args.star not in [1, 2]:
        raise InvalidArgument(f"{args.star} is not a valid choice for -s/--star")

    return args.day, args.star


def get_star_func(day, star):
    return DAYS[day]['star_funcs'][star-1]


def get_input_lines(day, per_line_func=None):
    with open(os.path.join(sys.path[0], f"day{day}/input.txt"), 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        if per_line_func:
            lines = [per_line_func(line) for line in lines]

        return lines


if __name__ == '__main__':
    day, star = get_day_and_star()
    star_func = get_star_func(day, star)

    if 'per_line_func' in DAYS[day]:
        input_lines = get_input_lines(day, DAYS[day]['per_line_func'])
    else:
        input_lines = get_input_lines(day)

    print(f"Output for day {day} star {star} is: {star_func(input_lines)}")
