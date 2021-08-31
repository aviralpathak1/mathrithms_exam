#pseudo code of logic.

'''
#for recursive function
quickSort(arr[], low, high)                      {this section defines the function of the quick short }
{
    if (low < high)                               {  checking the value of the one element to another }
    {
        pi = partition(arr, low, high);            { calling the function }

        quickSort(arr, low, pi - 1);  // Before pi     { recursive calling}
        quickSort(arr, pi + 1, high); // After pi       { again recursive calling}
    }

}

partition (arr[], low, high)                            {partition of the array }
{
   
    pivot = arr[high];                                  { if the pivot element is equals to high then do i to low-1 }
 
    i = (low - 1)  
    for (j = low; j <= high- 1; j++)                     {function for checking the othere element}
    {
        
        if (arr[j] < pivot)                               {condition checking}
       {
            i++;                                          {incrementing the value }
            swap arr[i] and arr[j]                        { swaping the value}
        }
    }
    swap arr[i + 1] and arr[high])                        {swaping the array element}
    return (i + 1)                                         
}


'''


#code for quick short 
def partition(start, end, array):
	

	pivot_index = start
	pivot = array[pivot_index]
	

	while start < end:
		

		while start < len(array) and array[start] <= pivot:
			start += 1
			

		while array[end] > pivot:
			end -= 1
		

		if(start < end):
			array[start], array[end] = array[end], array[start]
	

	array[end], array[pivot_index] = array[pivot_index], array[end]
	

	return end
	

def quick_sort(start, end, array):
	
	if (start < end):
		

		p = partition(start, end, array)

		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)
		

array = [ 83 , 1 , 45 , 95 , 45 , 52 , 11 , 470 , 45 , 67 , 82 ]
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')


