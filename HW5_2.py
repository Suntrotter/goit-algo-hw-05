def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return iterations, arr[mid]

    if right < 0:
        return iterations, arr[0]
    elif left >= len(arr):
        return iterations, None
    else:
        return iterations, arr[left] if arr[left] >= target else arr[left + 1] if left + 1 < len(arr) else None

sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
target_value = 1.0

result = binary_search(sorted_array, target_value)
print("Кількість ітерацій та верхня межа:", result)
