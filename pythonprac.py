def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left_half)
    right= merge_sort(right_half)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    l, r = 0, 0

    while l < len(left) and r< len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l+= 1
        else:
            result.append(right[r])
            r+= 1

    # Append any remaining elements from both lists
    result.extend(left[l:])
    result.extend(right[r:])

    return result

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
