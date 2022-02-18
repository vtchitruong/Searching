def search(myList, left, right, key):
    while left <= right:
        mid = (left + right) // 2 # floor division rounds down to the nearest whole number


        if myList[mid] == key:            
            return mid
        elif myList[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [24, 34, 41, 45, 58, 62, 64, 67, 69, 78]
l = 0
r = len(arr) - 1
k = 64

result = search(arr, l, r, k)
if (result == -1):
    print('Phần tử cần tìm không tồn tại trong danh sách.')
else:
    print('Tìm thấy tại vị trí: ', result)