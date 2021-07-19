"""
This is the code for a simple
bubble sort of an array
which prints out each step of the array sorting itself
"""


def BubbleSort(array):
    swap = "yes"
    while swap == "yes":
        swap = "no"
        for k in range(len(array)-1):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]
                print(array)
                swap = "yes"
    print("HERE IS FINAL ANSWER\n")
    print(array)

print(BubbleSort([4,3,2,1,6,4,5,7,8]))
