# Divide and Conquer Algorithm (5th week)

#Inversion /////
"""def Invers(arr):
    result=0
    for i in range (len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                result+=1
    return result

arr = [21,70,36,14,25]
    
result=Invers(arr)
print(result)"""


#Min-Max (Divide&Conquer)
"""arr = [3,7,5,2,1,8,9]
total = 0
for i in range(len(arr)):
    total = total+arr[i]
    
print(total)"""

"""def dnc_Max(arr,idx,len):
    maxi = -1
    
    if(idx>=len-2):
        if(arr[idx]>arr[idx+1]):
            return arr[idx]
        else:
            return arr[idx+1]
        
    maxi = dnc_Max(arr,idx+1,len)
    if (arr[idx]>maxi):
        return arr[idx]
    else:
        return maxi
    
def dnc_Min(arr,idx,len):
    mini = 0
    if(idx>=len-2):
        if(arr[idx]<arr[idx+1]):
            return arr[idx]
        else:
            return arr[idx+1]
        
    mini = dnc_Min(arr,idx+1,len)
    if(arr[idx]<mini):
        return arr[idx]
    else:
        return mini
    
if __name__ == '__main__':
    mini,maxi = 0 , -1
    
    arr = [4,12,23,9,21,1,35,2,24]
    maxi = dnc_Max(arr,0,9)
    mini = dnc_Min(arr,0,9)
    print("\nmaximum num = ",maxi)
    print("minimum num = ",mini)"""
    
# Merge-Sort

"""def mergeSort(arr):
    if len(arr)>1:
    
        r=len(arr)//2
        L=arr[:r]
        M=arr[r:]

        mergeSort(L)
        mergeSort(M)
    
        i=j=k=0
    
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=M[j]
                j+=1
            k+=1
        
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
            
        while j<len(M):
            arr[k]=M[j]
            j+=1
            k+=1

def cetakList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__ == '__main__':
    arr = [4,12,23,9,21,1,35,2,24]
    
    mergeSort(arr)
    print("\n  Sorted array : ")
    cetakList(arr)"""
    
# Quick Sort

"""def partition(arr,low,high):
    
    pivot= arr[high]
    
    i = low-1
    
    for j in range(low,high):
        if arr[j] <= pivot:
            
            i+=1
            
            (arr[i],arr[j]) = (arr[j], arr[i])
            
    (arr[i+1],arr[high]) = (arr[high],arr[i+1])
    return i+1

def quickSort(arr,low,high):
    if low<high:
        
        pi = partition(arr,low,high)
        
        quickSort(arr,low,pi-1)
        
        quickSort(arr,pi+1,high)
        
data = [4,12,23,9,21,1,35,2,24]
print("\n Unsorted array : ")
print(data)

size = len(data)

quickSort(data,0,size-1)

print("\n Sorted array in Ascending Order: ")
print(data)"""

# Tanpa Divide & Conquer

"""def maxSubSum(arr):
    max_so_far=0
    max_ending_here=0
    for i in range(len(arr)):
        max_ending_here+=arr[i]
        if max_ending_here>max_so_far:
            max_so_far=max_ending_here
        if max_ending_here<0:
            max_ending_here=0
    return max_so_far

arr=[-2,-5,6,-2,-3,1,5,-6]
result=maxSubSum(arr)
print(result)"""
            
# Dengan Divide and Conquer
def MaxCrossingSum(arr, low, mid, high):
  result = 0; leftSum=float('-infinity')
  for i in range(mid, low-1, -1):
    result+=arr[i]
    if result>leftSum:
      leftSum = result

  result = 0; rightSum=float('-infinity')
  for i in range(mid+1, high+1):
    result += arr[i]
    if result > rightSum:
      rightSum=result
  return leftSum + rightSum

def maxSum(arr,low,high):
  if low == high:
    return arr[low]
  mid = (low+high)//2
  return max(maxSum(arr,low,mid), maxSum(arr, mid+1, high), MaxCrossingSum(arr,low,mid,high))


arr = [-2,-5,6,-2,-3,1,5,-6]
result=maxSum(arr,0,len(arr)-1)
print(result)

# Longest Common Prefix

def comPrefix(a):
    
    size=len(a)
    
    if (size == 1):
        return a[0]
    
    a.sort()
    
    end=min(len(a[0]),len(a[size-1]))
    
    i=0
    while(i<end and a[0][i] == a[size-1][i]):
        i+=1
    
    pre = a[0][0:i]
    return pre

arr=["geeks4geeks","geeks","geek","geezer"]
result = comPrefix(arr)
print(result)

# Median dari dua array dengan Divide & Conquer

def medOfArray(arr1,arr2,n):
    m1=-1
    m2=-1
    count=0
    i=j=0
    while count<n+1:
        count+=1
        if i==n:
            m1=m2
            m2=arr2[0]
            break
        if j==n:
            m1=m2
            m2=arr1[0]
            break
        if arr1[i]<arr2[j]:
            m1=m2
            m2=arr1[i]
            i+=1
        else:
            m1=m2
            m2=arr2[j]
            j+=1
    return (m1+m2)//2

arr1 = [1,12,15,26,38]
arr2 = [2,13,17,30,45]

print(medOfArray(arr1,arr2,len(arr1)))

# Median dari dua array urut berbeda ukuran

def Solution(arr):
    n = len(arr)
    
    if n % 2 == 0:
        z = n//2
        e = arr[z]
        q = arr[z-1]
        ans = (e+q) /2
        return ans
    else:
        z = n//2
        ans = arr[z]
        return ans
    
arr1 = [-5,3,6,12,15]
arr2 = [-12,-10,-6,-3,4,10]
arr3 = arr1 + arr2

arr3.sort()
print("Median = ",Solution(arr3))

# Floor in sorted array

def floorSorted(arr,low,high,x):
    if low>high:
        return -1
    if arr[low]>x:
        return -1
    if arr[high]<=x:
        return arr[high]
    
    mid=(low+high//2)
    if arr[mid]==x:
        return arr[mid]
    if mid>0 and x>=arr[mid-1] and arr[mid]>x:
        return arr[mid-1]
    if mid<high and x <arr[mid+1] and x>=arr[mid]:
        return arr[mid]
    if x>arr[mid]:
        return floorSorted(arr,mid+1,high,x)
    else:
        return floorSorted(arr,low,mid-1,x)
    
arr = [1,2,8,10,12,14,19]
x=5
print(floorSorted(arr,0,len(arr)-1,x))

# Nilai terdekat dengan metode Divide & Conquer

def closest(arr,low,high,x):
    if low>high:
        return -1
    if arr[high]<=x:
        return arr[high]
    if arr[low]>=x:
        return arr[low]
    mid=(low+high)//2
    if arr[mid]==x:
        return arr[mid]
    abs_mid=abs(arr[mid]-x)
    if mid>0:
        abs_left=abs(arr[mid-1]-x)
        if abs_left<abs_mid:
            return closest(arr,mid+1,high,x)
        
    return arr[mid]

arr = [2,5,6,7,8,8,9]
x = 9
print(closest(arr,0,len(arr)-1,x))

# cara lain mencari nilai terdekat
def findClosest(lst,k):
    lst.sort()
    closest_num = lst[0]
    for num in lst:
        if abs(num-k) < abs(closest_num-k):
            closest_num=num
        if num>k:
            break
        return closest_num
lst = [3.64,5.2,9.42,9.35,8.5,8]
k = 9.1
print(findClosest(lst,k))
"""lst = [2,5,5,7,8,8,9]
k=6
print(findClosest(lst,k))"""

# Fixed point dengan Divide & Conquer

def fixedPoint(arr,low,high):
    if low>high:
        return -1
    if arr[high]==[high]:
        return arr[high]
    if arr[low]==low:
        return arr[low]
    mid=(low+high)//2
    if arr[mid]==mid:
        return arr[mid]
    if mid>arr[mid]:
        return fixedPoint(arr,mid+1,high)
    else:
        return fixedPoint(arr,low,mid-1)
    
arr = [9,1,4,5,2]
print(fixedPoint(arr,1,len(arr)-1))

# Divide and Conquer Algorithm
