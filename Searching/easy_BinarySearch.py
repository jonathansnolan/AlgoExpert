def binarySearch(array, target):
    L = 0
    R = len(array)
    M = (L+R)//2
    while array[M] != target:
        print(array[L:R])
        if target in array[L:M]:
            R = M
        else:
            L = M
        M = (L+R)//2
        print(array[L:R])
        if len(array[L:R+1]) == 2:
            if array[L] == target:
                M = L
            elif array[R-1] == target:
                M = R-1
            else:
                M = -1
            break
        return M

print(binarySearch([1,2,4,3,4,8,4,5,6,6,8,8,8,7,7,7,7,8,8,8,8,8,5,55,22,33,44,55,100], 3))
