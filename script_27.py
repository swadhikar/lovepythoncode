all([True, True, True, True])       # True
all([True, False, True, True])      # False

sports = ['cricket', 'football', 'tennis', 'rugby']

# Custom generator that stores sports names of size > 5
sizes_gt_5 = ( len(sport) > 5 for sport in sports ) # <generator object>

print( all(sizes_gt_5) )      # False
