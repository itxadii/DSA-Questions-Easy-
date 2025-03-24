# Find Maximum and Minimum – Find the largest and smallest number in an array.

def largestSmallest(arr):
    if not arr:
        return None 
    
    arr_max = arr_min = arr[-1]
    for num in arr:
        if num > arr_max:
            arr_max = num 
            
        if num < arr_min:
            arr_min = num
    return arr_max,arr_min

arr_max , arr_min = largestSmallest(arr="brina")    

print(arr_max,arr_min)