# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            print (f'j={j}')
            print(f'key={key}')
            print(f'arr[j]= {arr[j]}')
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# Driver code to test above
arr = [8,4,23,42,16,15]
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])

# This code is contributed by Mohit Kumra


insertionSort(arr)
