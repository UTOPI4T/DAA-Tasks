print("\t\tTUGAS 4 (ASYNCHRONOUS)\n")
#1 Latihan Swap /////
var1 = 11
var2 = 22
var3 = 33
print(" Before =", var1,var2,var3)
#_______
swap_func = var1, var2, var3 = var3, var2,var1
print("|After =",swap_func)

#2 Latihan Bubble Sort /////
list = [100,20,60,90,40,30,10]
print("\n Isi List\t=",list)
#_______
def BubSort(list):
    
    lastElemIdx = len(list)-1
    for passNo in range(lastElemIdx,0,-1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1]=list[idx+1],list[idx]
                
    return list

print("|Bubble Sorting =",BubSort(list))

#3 Latihan Insertion Sort /////
list = [89,12,57,16,25,11,75]
print("\n Isi List\t=",list)
#_______
def InsSort(list):
    for i in range(1, len(list)):
        j = i-1
        next = list[i]
        
        while (list[j] > next) and (j >= 0):
            list[j+1] = list[j]
            j-=1
        list[j+1] = next
    return list

print("|Insertion Sort =", InsSort(list))

#4 Latihan Selection Sort /////
list = [89,12,57,16,25]
print("\n Isi List\t=",list)
#_______
def SelSort(list):
    for fill in range(len(list)-1,0,-1):
        max_idx = 0
        for loc in range(1,fill+1):
            if list[loc] > list[max_idx]:
                max_idx = loc
        list[fill],list[max_idx] = list[max_idx],list[fill]
    return list

print("|Selection Sort =", SelSort(list))

#5 Linear Search /////
list = ['y','u','i','w','o','a','q','u','j','p']
#_______
def LinSearch (list,item):
    idx = 0
    found = False
    
    while idx < len(list) and found is False:
        if list[idx] == item:
            found = True
        else:
            idx += 1
    return found

print("\n|Linear Search a =",LinSearch(list, 'a'))
""" 
print(" Nilai A \t=",LinSearch(list, 'A'))
print(" Nilai '' \t=",LinSearch(list, ''))
print(" Nilai u \t=",LinSearch(list, 'u'))
"""

#6 Latihan Binary Search /////
list = ['y','u','i','w','o','a','q','u','j','p']
#_______
def BubSort(list):
    
    lastElemIdx = len(list)-1
    for passNo in range(lastElemIdx,0,-1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1]=list[idx+1],list[idx]
                
    return list
def BinSearch(list,item):
    first = 0
    last = len(list)-1
    found = False
    
    while first<=last and not found:
        mid = (first+last)//2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid-1
            else:
                first = mid+1
    return found

print("\n Setelah sorting =",BubSort(list))
print("|Binary Search a =",BinSearch(list,'a'))


#7 Latihan Interpolation Search /////
list = ['y','u','i','w','o','a','q','u','j','p']
#_______

def InterpolSearch (list,x):
        idx0 = 0
        idxn = (len(list)-1)
        found = False
        while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
            mid = idx0+int(((float(idxn-idx0)/(list[idxn]-list[idx0])) * (x-list[idx0])))
            
            if list[mid] == x:
                found = True
                return found
            
            if list[mid] < x:
                idx0 = mid+1
                
        return found

print("\n|Interpolation Search u =",InterpolSearch(list,'u'))

# Sorting & Searching #
