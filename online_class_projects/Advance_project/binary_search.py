
#project 5 binary search

def binary_search(arr, n):
    l, u = 0, len(arr) - 1

    while l <= u:
        mid = (l + u) // 2
        print(f"Checking middle index {mid}: {arr[mid]}")  # Debugging Step

        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            l = mid + 1
        else:
            u = mid - 1

    return -1

# User Input
arr = sorted([4, 7, 8, 12, 45, 99, 102, 702, 10987, 56666])
print("Sorted List:", arr)  # Debugging

n = int(input("Enter number to search: "))
print(f"Searching for: {n}")

# Perform Search
pos = binary_search(arr, n)

if pos != -1:
    print(f"🎯 Found at position {pos + 1}")
else:
    print("❌ Not Found")
