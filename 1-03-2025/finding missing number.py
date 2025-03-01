def find_missing_number(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)

n = input("Enter the numbers : ")
numbers = list(map(int, n.split()))
n = int(input("Enter the maximum number (n): "))
print(find_missing_number(numbers, n))
