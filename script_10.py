acct_balance_db = {
    'acct_1': 1000,
    'acct_2': 2000,
    'acct_3': 1500,
}

def deposit_salary(*acct_list, amount):
    print(type(acct_list))    # <class 'tuple'>

    """
        If not tuple, acct_list can potentially be modified and hacked!
        In order to ensure the callers of this API, unpacks to tuple
        which is an immutable datatype
    """
    # acct_list[0] = 'fake_acct'  # TypeError: tuple item assignment

    for acct in acct_list:
        acct_balance_db[acct] += amount  # increment each acct balance


if __name__ == '__main__':
    deposit_salary('acct_1', 'acct_2', 'acct_3', amount=500)

    print(acct_balance_db)  # {'acct_1': 1500, 'acct_3': 2000, 'acct_2': 2500}
