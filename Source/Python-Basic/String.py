"""
* Untuk membuat tipe Data String kita cukup melampirkan karakter dengan tanda kutip
* baik tanda kutip tunggal atau ganda ('', "")
"""
print('hello')
print("hello!")
print("hello, 'welcome' to 'UBK University'")

name = "tom" # * String
mychar = 'a' # * Character

print(name)
print(mychar)

name1 = str() # * ini akan membuat objek string kosong
name2 = str("newString") # * objek string yang berisi 'newString'

print(name1)
print(name2)

# * dengan menggunakan konstruktor str() kita juga dapat merubah tipe data lain menjadi string
angka = 20
print(angka)
print(type(angka))
angka = str(angka)
print(angka)
print(type(angka))

# * Manipulasi String menggunakan fungsi yang tersedia
print("\nManipulasi String")
myString = "Selamat Belajar Bahasa Python!"
myString1 = "Selamat Belajar, Bahasa Python!"
print(myString.capitalize()) # * mengubah huruf awal String akan berubah menjadi huruf Capital
print(myString.lower()) # * mengubah seluruh String menjadi huruf kecil
print(myString.upper()) # * mengubah seluruh String menjadi huruf besar
print(myString.find("jar")) # * mencari posisi huruf yang dicari dan mengembalikan nilai index posisi huruf yang di cari
print(myString.replace("Selamat", "Welcome")) # * mengganti suatu String (string yang akan diubah, string baru)
print(myString.split()) # * memisahkan kumpulan String
print(myString1.split(",")) # * memisahkan kumpulan String
print(myString.split("a")) # * memisahkan kumpulan String
print("a" in myString) # * mencari karakter String yang akan mengembalikan nilai Boolean
print("x" in myString) # * mencari karakter String yang akan mengembalikan nilai Boolean

# * Mengakses nilai dalam String
print("\nAkses String")
print("akses[0]:", myString[0])
print("akses[16]:", myString[16])
print("akses[-1]:", myString[-1])
print("akses[0:7]:", myString[0:7])
print("akses[:15]:", myString[0:15])

# * Update String
message = "Hello World"

print("Updated String: ", message[:6] + "Python")

first_name = "Joko"
last_name = "Saputro"

print(f"Hello {first_name} {last_name}")
print(f"Last Name is {last_name}")
