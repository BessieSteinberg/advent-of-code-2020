class PolicyPassword:
    def __init__(self, s):
        policy, self.password = s.split(":")
        self.min_occurrence, rest = policy.split('-')
        self.max_occurrence, self.letter = rest.split(' ')

        self.min_occurrence = int(self.min_occurrence)
        self.max_occurrence = int(self.max_occurrence)

    def is_valid(self):
        occurrence = 0

        for c in self.password:
            if c == self.letter:
                occurrence += 1

        return self.min_occurrence <= occurrence <= self.max_occurrence


def is_password_valid(s):
    return PolicyPassword(s).is_valid()


def count_valid_passwords(policy_password_list):
    ret_val = 0
    for s in policy_password_list:
        if is_password_valid(s):
            ret_val += 1

    return ret_val
