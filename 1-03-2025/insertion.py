def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
print(list_intersection(l1, l2))  
