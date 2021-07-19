def InsertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1],array[j]
                print(array)
                j -= 1
    print("HERE IS FINAL ANSWER\n")
    print(array)

print(InsertionSort([4,3,2,1,6,4,5,7,8]))
