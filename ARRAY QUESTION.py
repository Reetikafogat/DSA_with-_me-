# 1.Remove duplicates from  array/list inplace in python 
# there can be two cases a sorted array and a unsorted array .Incase of sorted array we can check adjacent element using two pointers if equal elements  just increment j else we first increment i and 
# then we equate  arr[i] to arr[j] (changing the elements inplce in the array. At the end we slice the array as till ith index the array will be sorted but after that index the array will contain duplicates
# so slice the array till i or ith+1 index based on the paarticular case. 
# 📍 Sorted array=
arr=[2,2,3,3,4,5,5]
i=0
for j in range(1,len(arr)):
  if arr[i]!=arr[j]:
    i+=1
    arr[i]=arr[j]
arr[:]=arr[:i+1]
print(arr) 

# 📍for unsorted array we need to make set which will keep track of that unique elements are only positioned in array and at the end slice the array.
arr=[2,4,3,2,1,5,5,4]
index=0
seen=set()
for i in array:
  if i not in seen:
    seen.add(i)
    arr[index]=i
    index+=1
arr[:]=arr[:index]
print(arr)
