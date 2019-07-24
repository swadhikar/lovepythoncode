<<<<<<< HEAD
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
=======
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter 
import sys

shoes = int(next(sys.stdin))
size_list = next(sys.stdin).split()
customers = int(next(sys.stdin))
size_cost_list = [tuple(t.split()) for t in sys.stdin]


def calculate_income(shoes, size_list, customers, size_cost_list):
    income = 0
    c = Counter(size_list)
    for size, cost in size_cost_list:
      cost = int(cost)
      if c[size]:
        income += cost
        c[size] -= 1
    return income

income = calculate_income(
  shoes, 
  size_list, 
  customers, 
  size_cost_list
)

print(income)
>>>>>>> ccebd816f43da5fbbae66f8677cd5ccbc1ce2ef5
