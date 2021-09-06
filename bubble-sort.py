unsorted_array = []
number = 0
#User input
print("Enter a set of numbers to sort. Enter -1 to stop")
while number != -1:
    number = int(input("Enter number: "))
    if number == -1:
        break
    unsorted_array.append(number)

#Bubble sort function
def bubble_sort(unsorted_array):
    length = len(unsorted_array)
    for i in range(length):
        for j in range(0, length - i - 1):
            if unsorted_array[j] > unsorted_array[j + 1]:
                unsorted_array[j], unsorted_array[j + 1] = unsorted_array[j + 1], unsorted_array[j]

    return unsorted_array


print("Printing sorted array..")
#driver code for sorting list
sorted_array = bubble_sort(unsorted_array)
print(sorted_array)
