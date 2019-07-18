def log_args(function):
    """Decorator function that logs function info"""
    print('*' * 35 + '\nFunction     :', function.__name__)

    def wrapper(*args, **kwargs):
        print('Arguments    :', args)
        print('Keyword args :', kwargs)
        print('*' * 35)

    return wrapper


@log_args                                   # Decorate 
def test_me(num_1, num_2, **kwargs):
    pass


test_me(10, 15, operation='-')              # Sample invocation
# ***********************************
# Function     : test_me
# Arguments    : (10, 15)
# Keyword args : {'operation': '-'}
# ***********************************
