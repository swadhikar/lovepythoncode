import re

text = "We$l&co*me&&t$op!rogr*a)(mm)(i)ng"

iter_obj = re.finditer('\w', text)
print(iter_obj)                         # <callable_iterator object>

for character in iter_obj:
    print(character.group(), end='')   #  Welcometoprogramming
print()
