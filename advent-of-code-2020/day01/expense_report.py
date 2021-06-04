def find_2020_sum(expenses):
    expenses_set = set()

    for expense in expenses:
        difference = 2020 - expense
        if difference in expenses_set:
            return expense, difference
        else:
            expenses_set.add(expense)

    raise AttributeError("No two values sum to 2020")


def prod_of_2020_sum(expenses):
    expense1, expense2 = find_2020_sum(expenses)
    return expense1 * expense2
