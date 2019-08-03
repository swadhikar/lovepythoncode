def print_welcome(num1, num2, design='.|.', text='WELCOME'):
    mid = num1 // 2
    pvt = 1
    fmt = '{:-^%d}' % num2

    for ln_no in range(num1):
        if ln_no == mid:
            print(fmt.format(text))
            continue

        if ln_no < mid:
            n_times = 1 + 2 * ln_no
            pvt = ln_no
        else:
            n_times =  1 + 2 * pvt
            pvt -= 1

        design_fmt = '{:-^%d}' % num2
        print(design_fmt.format(n_times * design))


if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print_welcome(num1, num2, design='*|*', text='GOOD DAY')
    print()
    print_welcome(num1, num2)

"""
9 27
------------*|*------------
---------*|**|**|*---------
------*|**|**|**|**|*------
---*|**|**|**|**|**|**|*---
---------GOOD DAY----------
---*|**|**|**|**|**|**|*---
------*|**|**|**|**|*------
---------*|**|**|*---------
------------*|*------------

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
