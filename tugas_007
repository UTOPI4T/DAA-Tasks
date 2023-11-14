"""x = 0
for x in range(2):
    x=x+2
    print(x)
    if (x==1):
        x=x+1
print("\n",x)"""

# Perkalian Matriks
mat1 = [ [2,4],
         [3,1],]
mat2 = [ [7,2],
         [5,6],]
mat3 = []

for x in range (0,len(mat1)):
    row = []
    for y in range (0,len(mat1[0])):
        total = 0
        for z in range (0, len(mat1)):
            total = total + (mat1[x][z]* mat2[z][y])
        row.append(total)
    mat3.append(row)

for x in range(0, len(mat3)):
    for y in range (0, len(mat3[0])):
        print(mat3[x][y], end=' ')
    print()

# Faktorial
def faktorial(n):
    if (n==1):
        return n
    return faktorial(n-1)*n

n = int(input("Input nilai n: "))
print(f"hasil dari {n}!", faktorial(n))

# Mencari elemen terbesar dan terkecil
a = [3, 20, 100, -35, 50]

def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def nilai_minimum(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai
    return nilai_terkecil

print("| Mencari nilai terbesar dan terkecil |\n", a)
print(" Nilai terbesar : ", nilai_maksimal(a))
print(" Nilai terkecil : ", nilai_minimum(a))


# Sequential Search
def SeqSearch(alist,item):
    pos=0
    found=False
    
    while pos < len(alist) and not found:
     if alist[pos] == item:
         found = True
     else:
      pos = pos+1
    return found

testlist = [1,2,32,8,17,19,42,13,0]
print(SeqSearch(testlist,3))
print(SeqSearch(testlist,2))


# Bubble Sort
alist = [54,26,93,17,77,31,44,55,20]
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

bubbleSort(alist)
print("\n",alist)

# Uji Keprimaan
x = int(input('| Input satu bilangan bulat : '))

angka_prima = True
if ((x==0) or (x==1)):
    angka_prima = False
else:
    for i in range (2,(x//2)):
        if((x % 1) == 0):
            angka_prima = False
            break
if(angka_prima):
    print(x, " adalah bilangan prima")
else:
    print(x," bukan bilangan prima")

# Hitung Polynominal
a = [1,2,0,3]
x = 1.5
def poly_py(a,x):
    result=0

    for n, a_n in enumerate(a):
        x_power_n = 1
        for i in range(n):
            x_power_n *= x
        result += a_n * x_power_n
    return result
print(poly_py(a,x))

test_str = "GFG is good website"
test_list = ["GFG","site","CS","Geeks","Tutorial"]

print("The original string is : "+test_str)

print("The original list is : "+str(test_list))

res = [sub for sub in test_list if sub in test_str]

print("The list of found substrings : "+str(res))

# Mencari pasangan titik jarak terdekat

from math import sqrt
from random import randint
titik = []
n = int(input('Masukkan jumlah titik yang Anda cari jaraknya: '))
for i in range (0, n):
    titik.append([randint(0, 100), randint(0, 100)])
print('Titik:\n', titik)

def hitungjarak(lis):
    lisjarak = []
    for i in range (0, len(lis)-1):
        for j in range ( i+1, len(lis)):
            jarak = sqrt((lis[i][0]-lis[j][0])**2 + (lis[i][1] - lis[j][1])**2)
            lisjarak.append(jarak)
            print('Titik: ', lis[i], 'Titik: ', lis[j], ': ', jarak)
    return min(lisjarak)
print('Jarak terdekat:\n', hitungjarak(titik))

# Linear Search

def find_maximum(lst):
    max = None
    for el in lst:
        if max == None or el > max:
            max = el
    return max

test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]
print(find_maximum(test_scores))

# Pangkat

bilangan = int(input('Masukkan bilangan: '))
pangkat = int(input('Masukkan pangkat: '))

def hitung_pangkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitung_pangkat(bilangan, pangkat - 1)
    return bilangan

hasil = hitung_pangkat(bilangan, pangkat)
print(f'Hasil = {hasil}')


# Pertemuan 7
