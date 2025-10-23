def mergeSort(arr):
	if len(arr) > 1:
		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements into 2 halves
		L = arr[:mid]
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Test the merge sort implementation
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)
mergeSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")

