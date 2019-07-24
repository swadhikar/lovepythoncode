def calculate_and_log(*args, calc_func=sum, log_func=print):
    result = calc_func(args)                    # complex arithmetic
    log_func(result)                            # logging logic

def store_to_db(value):
    # Logic to stored in db
    print('{} stored in db!'.format(value))

def write_to_file(value):
    # Logic to open file and write
    print('{} logged into file!'.format(value))

calculate_and_log(1, 2, 3)                       # 6 (in console)
calculate_and_log(1, 2, 3, log_func=store_to_db) # 6 stored in db!
calculate_and_log(1, 2, log_func=write_to_file)  # 3 stored in db!
