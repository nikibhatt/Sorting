# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i +1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        if arr[cur_index] > arr[smallest_index]:
            temp = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr

# import random
#
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
output1 = selection_sort(arr1)
output2 = bubble_sort(arr1)
print(output1)
print(output2)
#
# arr2= [0, 1, 2, 3, 4, 5]
# output1 = selection_sort(arr2)
# output2 = bubble_sort(arr2)
# print(output1)
# print(output2)
#
# arr4 = random.sample(range(200), 50)
# output1 = selection_sort(arr4)
# output2 = bubble_sort(arr4)
# print(output1)
# print(output2)
