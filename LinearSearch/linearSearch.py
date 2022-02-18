def search(myList, n, key):
    for i in range(n):
        if myList[i] == key:
            return i
    return -1 # Finish iterating the list

arr = [41, 67, 34, 69, 24, 78, 58, 62, 64, 45]
n = len(arr)
k = 62

result = search(arr, n, k)
if (result == -1):
    print('Phần tử cần tìm không tồn tại trong danh sách.')
else:
    print('Tìm thấy tại vị trí: ', result)