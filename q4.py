
tuples_list = [ (1, "a"), (2, "b"), (3, "c"), (1, "d") ]

target_set = {1, 3}  

res = [tup for tup in tuples_list if tup[0] in target_set]
print (res)
