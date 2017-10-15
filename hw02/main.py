def bsearch(data, target):
    if len(data) == 0:
        return None
    left = 0
    right = len(data) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if data[mid] < target:
            left = mid + 1
        elif data[mid] > target:
            right = mid - 1
        else:
            return mid
    return None
