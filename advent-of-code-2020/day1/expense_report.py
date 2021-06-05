def find_sum_pair(expenses, sum_total=2020):
    expenses_set = set()

    for expense in expenses:
        difference = sum_total - expense
        if difference in expenses_set:
            return expense, difference
        else:
            expenses_set.add(expense)

    raise AttributeError("No two values sum to 2020")


def prod_of_2020_sum(expenses):
    expense1, expense2 = find_sum_pair(expenses)
    return expense1 * expense2


def prod_of_2020_3_val_sum(expenses):

    for ii in range(len(expenses)):
        expense1 = expenses[ii]
        difference = 2020 - expense1

        try:
            expense2, expense3 = find_sum_pair(expenses[ii+1:], difference)
            return expense1 * expense2 * expense3

        except AttributeError:
            pass

    raise AttributeError("No three values sum to 2020")
