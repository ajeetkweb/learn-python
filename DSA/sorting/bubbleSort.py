

def bubbleSort(array):
    n = len(array)

    #loop to access each array Element
    for i in range(n):

        # keep tracking of swapping
        swapped = False

        # loop to compare array elements
        for j in range(0, n-i-1):

            # compare adjacent array elements
            if array[j] > array[j+1]:

                # swapping elements if 
                # elements are not in sorted order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True

            # no swapping means the array is already sorted
            # so no need for further comparison    
            if not swapped:
                break


data = [10,5,4,3]
bubbleSort(data)

print("Sorted Array in ascending order:")
print(data)


"""
No of comparision: n(n-1)/2

Time Complexity:
    Best	O(n)
    Worst	O(n2)
    Average	O(n2)
"""