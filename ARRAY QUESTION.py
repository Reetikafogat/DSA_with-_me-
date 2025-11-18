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
🏆# 3.Reverse an array in groups of k length 
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
🏆# 4.Rotate an array - rotate the array with d place .
#📍 simple approach: will be to put a for loop to run d time and other to write in the logic of shifting the places of elements, but it would take o(n*d) time complexxity and space complexity of o(1)
def rotate_arr(arr,d):
  n=len(arr)
  for i in range(d):
    temp=arr[i]
    for j in range(n-1):
      arr[j]=arr[j+1]
    arr[n-1]=temp
  return arr
#📍 the second approach would be to reverse the first d elements and then the remaining will be n-d elements then rotate them using reverse fuction and then reverse the whole array again to make 
# the elements reversed of the group and n-d in correct order.
def rotate(arr,d):
  n=len(arr)
  d=d%n
 🏆# 5.Maximum product of a triplet (subsequence of size 3) in array
# we need to find the maximum product possible in an array using 3 elements.this array contain +ve and -ve both elements, now the thing to remember is that alwys the positive product will be the highest(maximum)
# then the negative and that can come from two ways: multiplying three negatives will yield negative product so two negatives and the largest positive can yield max positive product and second is 
# multiplying the largest 3 numbers in the array 

# 📍using three nested loops: time---o(n3) and space----o(1)
arr=[-3,-6,1,5,6,2,1]
def max_product(arr):
  n=len(arr)
  product= -10**3
  for i in range(n-2):
    for j in range(i+1,n-1):
      for k in range(j+1,n):
        product=max(product,arr[i]*arr[j]*arr[k])
  return product
  
📍#using better approach -by sorting:time----o(nlogn) and space----o(1)
# sort the array first in ascending order then take two negatives and 1st largest for product compare it with the product of largest 3 +ve numbers 
def max_product(arr):
  arr.sort()
  return max(arr[0]*arr[1]*arr[n-1],arr[n-3]*arr[n-2]*arr[n-1])
  
📍# the optimal approach: find 3 largest in array and two smallest element in array using a single loop:time----o(n) and space---o(1)
def max_product(arr):
   first_largest=float('-inf')
   second_largest=float('-inf')
   third_largest=float('-inf')
  
   first_smallest=float('inf')
   second_smallest=float('inf')
  
   for i in range(n):
     if arr[i]>first_largest:
       third_largest=second_largest
       second_largest=first_largest
       first_largest=arr[i]
     elif arr[i]>second_largest:
       third_largest=second_largest
       second_largest=arr[i]
     elif arr[i]>third_largest:
       third_largest=arr[i]
       
     if arr[i]<first_smallest:
       second_smallest=first_smallest
       first_smallest=arr[i]
     elif arr[i]<second_smallest:
       second_smallest=arr[i]
       
    return max(first_smallest * second_smallest * first_largest, first_largest * second_largest * third_largest)

# 🏆 6.Maximum consecutive ones or zero's : can be done by two approach
# 📍using simple for loop and comaprison along with counting 
arr=[0,1,0,1,1,1,1,0,0,0,0,0]
count,max_count=0,0
for i in range(1,len(arr)):
  if arr[i]==arr[i-1]:
    count+=1
  else:
    max_count=max(count,max_count)
    count=0
proint(max_count)
# 📍using bit manipulation: use xor(^) which gives 0 if same no. else 1.

arr=[0,1,0,1,1,1,1,0,0,0,0,0]
count,max_count=0,0
  for i in range(1,len(arr)):
    if arr[i] ^ arr[i-1]==0:
      count+=1
    else:
      max_count=max(count,max_count)
      count=0
  print(max_count) 

# 🏆Move all zeroes to the end of array:
# 📍using a temporary array of length of array first put all non-zero to temp arr then fill the remaining space with zeroes.put  tracker (j) to find  the remaining space starting index.at last copy all the elements 
# to original in the order of temp array.
arr=[0,7,0,1,5,2,1,0]
n=length(arr)
j=0
for i in range(n):
  if arr[i]!=0:
    temp[j]=arr[i]
    j+=1
while j<n:
  temp[j]=0
  j+=1
for i in range(n):
  arr[i]=temp[i]

# 📍 using swapping:

j=0
for i in range(n):
  if arr[i]!=0:
    arr[i],arr[j]=arr[j],arr[i]
    j+=1
return arr
