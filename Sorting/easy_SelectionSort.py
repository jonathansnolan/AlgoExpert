def SelectionSwap(array):
    for i in range(0,len(array)-1):
        small = i
        for j in range(i+1, len(array)):
            if array[small] > array[j]:
                small = j
        if small != i:
            array[i], array[small] = array[small], array[i]
            print(array)
    print("HERE IS FINAL ANSWER\n")
    print(array)

print(SelectionSwap([4,3,2,1,6,4,5,7,8]))
