from collections import Counter

def most_frequent_element(lst):
    if not lst:
        return None 

    count = Counter(lst)  
    return count.most_common(1)[0][0]  

numbers = [1, 3, 2, 3, 4, 3, 5, 2, 2, 2, 2]
print("Most frequent element:", most_frequent_element(numbers))  
