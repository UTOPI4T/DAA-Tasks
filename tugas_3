# Tampilkan tanggal /////
import datetime

x = datetime.datetime.now()
# Dengan hari
print(f"\n{x:%A, %B %d %Y}"+"\n")
# Tanpa hari
#print(x.strftime("\n\t%B %d,%Y\n"))


# Latihan_List_Mahasiswa /////________________________________
#1 Buatlah list        >>>   (data "Mahasiswa")
Mahasiswa = ["Nathan R", 202207161,"Informatika","DAA", "UPJ"]
print("\nData \t\t=  "+str(Mahasiswa))

#2 Cetak NIM           >>>   (panggil index)
print("NIM \t\t= ",Mahasiswa[1])

#3 Cetak universitas   >>>   (panggil index)
print("Universitas \t= ",Mahasiswa[4])

#4 Cetak NIM dan Prodi >>>   (list slicing)
print("NIM dan Prodi \t= ", Mahasiswa[1:3], "\n")

#5 Cetak UPJ di depan  >>>   (iteration)
for plus in Mahasiswa:
    print("UPJ "+str(plus))



# Latihan_Tuples /////________________________________________
#1 Susun Tuple bernama "UPJ"
upj = ('Universitas','Pembangunan','Jaya')
print("\nSusunan tuple = ",upj)

#2 Nested Tuple dengan nilai :
pertama = ('100')
kedua = ('200','400','600')
ketiga= ('300')
keempat= ('400','800')
nested_tup = (pertama,kedua,ketiga,keempat)

print("\nNested tuple = ",nested_tup)
"""print(str(pertama)+str(kedua)+str(ketiga)+str(keempat))"""


#1 Latihan_Dictionary_(Nama, NIM, Prodi, Universitas)  ///// _______________
data = {'Nama': 'Nathan R',
      'NIM' : '2022071061',
      'Prodi':'Informatika',
      'Universitas':'UPJ'}

print("\n",data)

# Fungsi get 
print("\n NIM : ",data.get('NIM'))

# Update nilai 
data['Nama'] = 'Nathan R.P'
print("\n",(data))

# Latihan Set ///// ________________________________________________________
"""
# Materi Set dua himpunan 
set_A = {1,2,3,4}
set_B = {3,4,5,6}
print("A|B =", set_A | set_B) #Union (gabungan A dan B)
print("A&B =", set_A & set_B) #Intersection (irisan A dengan B)
print("A-B =", set_A - set_B) #A_Difference_B (nilai A)
print("B-A =", set_B - set_A) #B_Difference_A (nilai B)
print("A^B =", set_A ^ set_B) #A_symmetric_difference_B (nilai A dan B saja)
"""

#1 Latihan Set         >>>   (Union dan Intersection)
red    = {'dandelions', 'fire hydrant', 'leaves'}
yellow = {'fire hydrant','rose','blood','leaves', }

# Union red dan yellow
union_sets = red|yellow
print("\n Union =",union_sets)

#Intersection red dan yellow
intersec_sets = red&yellow
print("\n Intersection =",intersec_sets)

#1 Latihan dataframe mhs ///// ____________________________________
import pandas as pd
mhs = pd.DataFrame([['1', 'Informatika', 50, 30, 20],
                   ['2', 'Sistem Informasi', 55, 30, 25],
                   ['3', 'Teknik Sipil', 40, 30, 10]])

mhs.columns = ['No.', 'Prodi', 'Mahasiswa', 'Laki-laki','Perempuan']

print(mhs)

#1 Latihan Matrix to transpose matrix ///// _________________________
import numpy as np 
matrix = np.array([[100,200,300], [700,600,500],[900,1000,800]]) 
print("Matrix : \n",matrix,"\n")

#Transpose Matrix
transpose_matrix = np.transpose(matrix)
print("Transpose matrix :\n",transpose_matrix)

# Python Codes Tasks #
