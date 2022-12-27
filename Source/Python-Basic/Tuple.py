"""
* Tuples adalah tipe data dalam Python yang memiliki sifat immutable (tidak dapat diubah) berbeda dengan list yang bersifat mutable (dapat dirubah)
* Tuple sama halnya seperti list yang merupakan kumpulan berurut (sequence) namun yang membedakanya
* adalah isi dari tuples tidak dapat dirubah atau read-only dan menungkinkannya untuk duplikat
* Pendeklarasian tipe data tuple menggunakan tanda kurung () kemudian isi dari tuple dipisah dengan tanda koma
* misal : angka = (1, 2, 3, 4, 5)
* Operasi Method yang didukung tuple :
* - print(), index(), count(), len()
* Dengan menggunakan Tuple akan lebih hemat memori jika dibandingkan list
"""
myList = [1, "two", 3]
myTuple = (4, "five", 10, "six", "seven", 8, 9, 10, 10)

print(myList)
print(type(myList))
print(myTuple)
print(type(myTuple))

# * Access Tuple items
print("\nAccess Tuple items")
print("Nilai index elemen 'seven' dalam myTuple:", myTuple.index("seven"))
print("Niai index elemen 8 dalam myTuple dari index 2 sampai 6:", myTuple.index(8, 2, 6))
print(myTuple[1]) # * Access with index
print(myTuple[1:4]) # * Access with range index
print(myTuple[3:]) # * Access with slicing index
print(myTuple[:5]) # * Access with slicing index
print(myTuple[:-3]) # * Access with negative index
print(myTuple[-4:-1]) # * Access with range negative index

print("jumlah seluruh element / items pada myTuple sebanyak:", len(myTuple)) 
print(f"jumlah seluruh elemen myTuple with formating string: {len(myTuple)}")
print(f"jumlah banyaknya nilai 10 dalam item myTuple: {myTuple.count(10)}")
print(f"Nilai index pertama dari item 10: {myTuple.index(10)}")

# * Update Tuple
"""
* karena Tuple tidak dapat diubah, tambah ataupun menghapus elemen item, maka kita bisa menggunakan
* beberapa solusi seperti mengubahnya / mengkonvesi dari Tuple ke List, kemudian menyisipkan action (tambah, edit dan hapus)
* baru kemudian di konversi kembali dari List ke Tuple
"""
print("\nUpdate Tuple")
myConvert = list(myTuple) # * Convert Tuple to List
print(myConvert)
myConvert[2:9] = [6, "seven", 8, 9 , 10, 11, 12, 13] # * Update item on index 2
myTuple = tuple(myConvert) # * Convert List to Tuple
print(myTuple)

print("\nAdding item Tuple")
myConvert = list(myTuple) # * Convert Tuple to List
myConvert.append(14) # * Adding item list
myTuple = tuple(myConvert) # * Convert List to Tuple
print(myTuple)

print("\n Adding Tuple to Tuple")
myTuple += ("fifteen",) # * untuk menambahkan satu item ingatlah untuk menyertakan tanda koma setelah item jika tidak maka tidak akan terindentifikasi sebagai Tuple
print(myTuple)

# * Perulangan Tuple
# * ada beberapa cara perulangan yang bisa dilakukan diantaranya:
# * - for loop, for loop by Index Number, While loop
print("\nLoop Tuple")
for i in myTuple:
    print(i)

print("\nLoop the Index Number")
for j in range(len(myTuple)): # * menggunakan fungsi range() dan len() untuk membuat iterable yang sesuai
    print(myTuple[j])

print("\nLooping with While Loop")
index = 0
while index < len(myTuple):
    print(myTuple[index])
    index += 1
    
# * Merge Two Tuple or More
# * Untuk menggabungkan 2 atau lebih Tuple kita bisa menggunakan operator '+' (plus) atau tambah
myTuple1 = (10, 20, 30, 40)
myTuple2 = (100, 200, 300, 400)
myTuple3 = (1000, 2000, 3000, 4000)

myTuple4 = myTuple1 + myTuple2 + myTuple3
print(myTuple4)

# TODO 1 : Coding Exercise Check-in: Python Tuples
# ? TASK : Tentukan Tuple bernama my_tuple yang bersisi (1, 2, 3, 4, 5), 
# ? -> kemudian tampilkan ouput dari elemen terakhir my_tuple apakah lebih kecil dari 10.
# ? Didalam function print() anda dapat menggunakan operator perbandingan sederhana yang mengembalikan
# ? -> nilai boolean (misal. x < 5)

# * Your Code Goes Here
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[-1] < 10)

# * Testing Code
if my_tuple is True:
    print("Great, your solution is correct!")
else:
    print("Your solution is not correct")

# TODO 2 : Coding Exercise Check-in: Python Tuples
# ? TASK : Gunakan rentang index untuk mencetak item ketiga , keempat dan kelima dalam tuple berikut:
# ? furniture = ("table", "chair", "rack", "shelf")

# * Your Code Goes Here