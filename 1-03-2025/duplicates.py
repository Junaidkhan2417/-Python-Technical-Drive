def remove_duplicates(lst):
    s1 = set() 
    re = []   

    for l in lst:
        if l not in s1:
            re.append(l)
            s1.add(l)

    return re


numbers = [1, 2, 2, 3, 4, 3, 5, 1, 6]
print("List without duplicates:", remove_duplicates(numbers)) 