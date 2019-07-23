in_list = [1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7]

# 1. Convert to dictionary of None values and rebuild list
in_list = list(   {item: None for item in in_list}.keys()   )
print( in_list )    # [1, 2, 3, 4, 5, 6, 7]

""" The results are from python 3.7 execution. List ordering may vary if ran from versions < 3.7 """
