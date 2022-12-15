"""
List adalah Struktur Data dalam Python yang dapat menampung pernyataan
dalam urutan yang ditentukan oleh tanda kurung dimana setiap elemen ditentukan oleh koma.
List juga dapat menampung berbagai jenis tipe data diantaranya seperti integer, float, dan string

contohnya : ["item", 0, 0.12, "some", myList]

List memungkin Anda untuk dapat melakukan operasi seperti menambah, menghapus, atau memproses elemen dengan cara yang sangat sederhana,
list sangat mirip dengan Array.
"""
myVar = 10
myList = [50, 70, 55, 100, 200, 201, 555, 300, 400, myVar]

print(myList)
# * Mengakses elemen didalam list menggunakan index
print(f"myList[2]:", myList[2])
print(f"myList[-2]:", myList[-2])

# * Mengakses elemen didalam list menggunakan teknik slicing
print(f"myList[0:3]:", myList[0:3])
print(f"myList[1:3]:", myList[1:3])

# * Kita juga bisa melakukan beberapa operasi dengan menggunakan metode yang umum digunakan dalam mengolah list seperti:
"""
append
count
extend
index
insert
remove
reverse
sort
pop
len
max
min
"""
myVarNew = "NEW"
myList.append(myVarNew)
print(f"myList.append(myVarNew):", myList)

myList.insert(0, myVarNew)
print(f"myList.insert(0, myVarNew):", myList)
myList.insert(2, myVarNew)
print(f"myList.insert(2, myVarNew):", myList)

print(myList)
myList.reverse()
print(f"myList.reverse()", myList)

myList.pop() # * jika elemen tidak ditentukan maka pop akan menghapus elemen terakhir dalam list
print(f"myList.pop():", myList)
print(myList)
elemen_removed = myList.pop(0), myList.pop(9)
print(f"myList.pop(2):", elemen_removed) # * element 2 ditentukan untuk di hapus

print(myList)
myList.sort()
print(f"myList.sort()", myList)

print(f"len(myList):", len(myList))

print(myList)
myList.remove(100) # * method remove akan menghapus nilai / item di dalam list berdasarkan nilai bukan berdasarkan index
print(f"myList.remove(100):", myList)

print(f"sebelum menghapus nilai pada index:", myList)
del myList[2] # * method del digunakan jika kita tahu persis elemen mana yang akan dihapus, jika kita tidak tahu persis kita bisa menggunakan metode remove()
print(f"setelah menghapus nilai di index ke 2:", myList)

print(f"nilai tertinggi didalam list:", max(myList))
print(f"nilai terendah didalam list:", min(myList))

myList1 = [99, 44]
myList.extend(myList1)
print(f"myList.extend(myList1):", myList)

# * List Comprehension
"""
List Comprehension digunakan untuk mempersingkat assignment data list dengan perulangan for
list Comprehension merupakan ternary operator pada Python yang berfungsi untuk mempersingkat proses inisialisasi variable list.
format penulisan List Comprehension : <variable-target> = [<kembalian> for <item> in <iterable>] atau bisa ditambahkan dengan kondisi : <variable-target> = [<kembalian> for <item> in <iterable> if <kondisi>]
Ket :
    - variable-target: variable untuk menampung list yang telah dibuat
    - kembalian: nilai yang akan dikembalikan sebagai elemen list. Dapat berupa nilai tetap, variable, maupun ekspresi untuk memproses nilai item
    - item: penampung nilai dari iterable pada tiap iterasi, nilai ini dapat digunakan sebagai ekspresi dalam kembalian
    - iterable: variable yang berisi kumpulan nilai (list, string, tuple, dll)
    - Jika terdapat if statement seperti format di atas maka nilai item hanya akan diproses ketika kondisi bernilai True
"""

# bentuk umum
list1 = []
for i in range(10):
    list1.append(i)
    # list1.append(i + 1)

print(f"bentuk umum:", list1)

list2 = [x for x in range(10)]
print(f"list comprehension:", list2)

list3 = [x + 1 for x in range(10)]
print(f"list comprehension:", list3)

list4 = [x for x in range(10) if x % 2 == 0]
print(f"list comprehension:", list4)

list5 = [x * 2 for x in range(10) if x % 2 == 0]
print(f"list comprehension:", list5)

# TODO 1 : Coding Exercise Check-in: Python Lists
# ? : Urutkan Daftar dan cetak tiga elemen pertama dari list berikut !
# ! unsorted_list = [123, 5, 4, 14215, 2, 6, 12467, 1, 923, 991, 42]
# Aswere :
unsorted_list = [123, 5, 4, 14215, 2, 6, 12467, 1, 923, 991, 42]
unsorted_list.sort()
print(unsorted_list[:3])

# TODO 2 : Coding Exercise Check-in: Python Lists
# ? : Tambahkan item 12, 8 dan 4, kemudian Ubahlah item ke-2 dari list menjadi 3 dari list berikut !
# ! y = [6, 4, 2]
# Aswere :
# Cara 1
y = [6, 4, 2]
y[len(y):] = [12, 8, 4]
y[1] = 3
print(y)

# Cara 2 
z = [6, 4, 2]
z.extend([12, 8, 4])
z[1] = 3
print(z)

# Cara 3 
x = [6, 4, 2]
for i in range(3, 4):
    x.extend([12, 8, 4])
    if x[1] == 4:
        x[1] = 3
    
print(x)

# cara 4 
g = [6, 4, 2]
g.append(12)
g.append(8)
g.append(4)
g[1] = 3
print(g)