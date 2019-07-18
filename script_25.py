
inlist = [7, 1, 2, 101, 203, 1000, 2000, 3000]
result = {1: 3, 3: 2, 4: 3}  # n(1 digit number)=3, n(3 digit number)=2

result = {}
for num in inlist:
    num_size = len( str(num) )    # len() doesn't work on int object
    result[num_size] = result.get(num_size, 0) + 1
print(result)
