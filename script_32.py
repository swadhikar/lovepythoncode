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
