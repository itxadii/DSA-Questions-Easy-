# Find the largest and smallest element in an array.
def LargestSmallest(arr):
    maxarr = arr[0]
    minarr = arr[0]
    for i in arr:
        if i > maxarr:
            maxarr = i
        if i < minarr:
            minarr = i
    return maxarr,minarr
        
min,max = LargestSmallest([4,58,8,1])
print(min,max)

