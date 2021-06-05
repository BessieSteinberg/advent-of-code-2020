class PolicyPassword:
    def __init__(self, s):
        policy, self.password = s.split(":")
        self.lo, rest = policy.split('-')
        self.hi, self.letter = rest.split(' ')

        self.lo = int(self.lo)
        self.hi = int(self.hi)

    def is_letter_in_pos(self, pos):
        if pos <= 0 or pos >= len(self.password):
            return False
        return self.password[pos] == self.letter

    def is_valid(self, policy):
        if policy == 1:
            occurrence = 0

            for c in self.password:
                if c == self.letter:
                    occurrence += 1

            return self.lo <= occurrence <= self.hi

        elif policy == 2:
            def logical_xor(a, b):
                return bool(a) ^ bool(b)

            is_letter_in_lo_pos = self.is_letter_in_pos(self.lo)
            is_letter_in_hi_pos = self.is_letter_in_pos(self.hi)

            return logical_xor(is_letter_in_lo_pos, is_letter_in_hi_pos)


        else:
            raise Exception("Policy must be 1 or 2")


def is_password_valid(s, policy):
    return PolicyPassword(s).is_valid(policy)


def count_valid_passwords(policy_password_list, policy):
    ret_val = 0
    for s in policy_password_list:
        if is_password_valid(s, policy):
            ret_val += 1

    return ret_val


def count_valid_passwords_policy_1(policy_password_list):
    return count_valid_passwords(policy_password_list, 1)


def count_valid_passwords_policy_2(policy_password_list):
    return count_valid_passwords(policy_password_list, 2)
