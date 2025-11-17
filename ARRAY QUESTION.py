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

#🏆2.reverse an array
# 📍using an another array - first create an empty array of same length as original array and then start looping from the end of original array and store every element in new array then again loop the new array and 
# change the items of original array with new array's elements 
arr=[1,2,3,4,5,6]
n=len(arr)
new_arr=[0]*n
for i in arr:
  new_arr[i]=arr[n-i-1]
for i in new_arr:
  arr[i]=new_arr[i]
return arr
#📍using reverse() function in python 
#📍using two pointers approach - start two pointers i and j i starts from beginning of array and j starts from the end of array and increment i and decrement j everytime the elements are swapped until i<j. 
i=0
j=n-1
while i<j:
  arr[i],arr[j]=arr[j],arr[i]
  i+=1
  j-=1
return arr
🏆# Reverse an array in groups of k length 
# for eg: arr=[1,2,3,4,5,6,7,8] then output [3,2,1,6,5,4,8,7]. if the elements remaining is not of length of k thyen just reverse it. so theapproach will bethat we comapare the length of arr or 
# elements remaining in array with the the reversed length or reversed no. of elements and thus find which one is less and if the reversed length is short that means thereare more elements outside reversed part of
# array and again the looping could be done and k length of elements would be reversed . for this we require two loops one for the length to iterate or creating subgroups and other to write the 
# reversing array logic using two pointers 
reversed_arr(arr,k):
n=len(arr)
i=0
while(i<=n):
  start=i
  end =min(i+k-1,n-1)
  while(start<end):
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1
  i+=k
return reversed_arr
