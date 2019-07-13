max = 5
itr = 2 * max + 1
counter = 1

for i in range(1, itr):
    if i < max + 1:
        print(i * '* ')
        continue
    count = max - counter
    print(count * '* ')
    counter += 1
