"""
* Penanganan file adalah bagian penting dari sebuah aplikasi
* Python memiliki beberapa fungsi untuk membuat, membaca, memperbaharui dan menghapus file
* Kunci fungsi yang digunakan untuk penangan berkas / file di Python adalah fungsi open()
* Untuk membaca/menulis ke file kita juga bisa menambahkan statement (pernyataan) "with". ini akan menutup file setelah selesai digunakan
* -> ini bisa menjadi alternatif penggunaan fungsi close()
* Fungsi open() membutuhkan dua parameter yakni : nama file dan mode
* ada 4 method (mode) yang digunakan untuk membuka file:
* - "r" : Read (Baca) -> Nilai default. Membuka file untuk dibaca, erorr jika file tidak tersedia
* - "a" : Append (Menambahkan) -> Membuka file untuk ditambahkan, membuat file jika tidak tersedia
* - "w" : Write (Menulis) -> Membuka file untuk menulis, membuat file jika tidak ada
* - "x" : Create (Membuat) -> Membuat file yang ditentukan, mengembalikan kesalahan jika file tersedia
* Selain itu ada dua mode tambahan yang bisa ditangani apakah sebagai biner atau teks
* - "t" : Text (Teks) -> Nilai default. mode Teks
* - "b" : Mode Biner (misalnya gambar)
* Ada beberapa Method Alternatif dalam File Handling diantaranya seperti:
* - read() : akan mengembalikan konten file
* - readable() : akan mengembalikan apakah file dapat dibaca atau tidak output Boolean (TRUE or FALSE)
* - readline() : akan mengembalikan satu baris dari file
* - readlines() : akan mengembalikan ke dalam bentuk baris list dari file
* - write() : menulis String yang ditentukan ke file
* - writable() : mengembalikan file apakah file dapat ditulis atau tidak
* - writelines() : menulis string list ke file


# * Open file on the Server
# * Asumsikan kita telah memiliki file yang terletak di folder yang sama dengan file Python, untuk membukanya kita bisa menggunakan 
# * -> fungsi bawaaan yakni fungsi open()
# * Mari buat terlebeih dahulu file dengan nama demofile.txt
print("Open file on the Server!")
file = open("demofile.txt", "r")
print(file.read())

# * Jika file berada di lokasi yang berbeda, kita harus menentukan jalur (path) file nya terlebih dahulu
print("\nOpen file in located different location")
f = open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/welcome.txt", "r")
print(f.read())

# * Menulis ke file yang tersedia
# * Untuk ini kita tetap akan menggunakan Method open(), tetapi ditambahkan dengan mode misal:
# * -> mode "a" atau "w"
# * Mode "a" (tambahkan): akan menambahkan ke akhhir file
# * Mode "w" (tulis) : akan menimpa konten seluruh kontent yang sudah ada
print("\n")
g = open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/demofile2.txt", "a")
# * write to the file
g.write("Test!, Menulis ke file demofile2.txt")
# * close the file
g.close()

# * Buka dan Baca file setelah ditambahkan
print("Open and Read File After appending")
g = open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/demofile2.txt", "r")
print(g.read())

# * Menulis dengan mode "w" : Tulis dan akan menimpa konten yang ada
g = open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/demofile2.txt", "w")
g.write("Woops!, I have deleted the content")
g.close()

# * Buka dan Baca file setelah ditambahkan
print("Open and Read File After appending")
g = open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/demofile2.txt", "r")
print(g.read())

# * Membuat file baru dengan mode "x" (Buat) : akan membuat file, mengembalikan kesalahan jika file tersebut tersedia
# print("\nMembuat file baru dengan mode 'x'")
# f = open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/newFile.txt", "x")
# print("Berhasil membuat file baru kosong!")

# * Cara selanjutnya bisa menggunakan statement 'with' untuk membaca dan menulis file
# * Dengan statement 'with' kita tidak perlu menambahkan method / fungsi close(), karena 'with' akan menutup file jika telah selesai digunakan
# * Dengan statement 'with' kita juga dapat menambahkan as (alias) untuk mempermudah
print("\nReading or Writing file use 'with' statement")
with open("demofile.txt") as DemoFile:
    content = DemoFile.read()

print(content)

# * Sebagai alternatif kita juga dapat menggunakan method / fungsi readlines() untuk mendapatkan nilai string list dari file. 1 string untuk setiap baris
print("\nUse Method readlines() to the file")
with open("demofile.txt") as DemoFile2:
    content2 = DemoFile2.readlines() # * akan mengembalikan semua baris file ke dalam bentuk item list

print(content2)
print(type(content2))

# * kita juga dapat melakukan perulangan baris demi baris pada sebuah file
print("\nMelakukan perulangan pada suatu file")
with open("demoFile.txt") as DemoFile3:
    for i in DemoFile3:
        print(i, end="")

print()
# * Menulis ke file menggunakan statement 'with'
print("\nMenulis ke file menggunakan statement 'with'")
with open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/demoFile.txt", "w") as DemoFile1:
    DemoFile1.write("Hello, World!\n")

with open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/demoFile.txt", "a") as DemoFile1:
    DemoFile1.write("Ini adalah teks ke-2 dalam file demoFile.text!")

with open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/demoFile.txt") as DemoFileRead:
    content3 = DemoFileRead.read()

print(content3)

print("\nMenulis file menggunakan Method writelines()")
with open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/newFile.txt", "w") as demoFile:
    f = demoFile.writelines(["See You Soon!\n", "Over and Out."])

with open("/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source/file/newFile.txt") as demoFile:
    f = demoFile.read()

print(f)
print(type(f))

"""
# * Kita juga dapat menghapus file caranya kita membutuhkan module OS
# * os.remove("<namefile>.txt") or os.remove("path/<namefile>.txt")
# * Sebaiknya sebelum file dihapus kita lakukan pengecakan terlebih dahulu sebelum file tersebut benar-benar akan kita hapus
print("\nMenghapus file")
import os
import shutil
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("File Has Been Removed Successfully")
else:
    print("The file does not exist")

# * Menghapus folder
print("\nMenghapus folder")
directory = "file"
parrent = "/Users/peduthui/Documents/Activity/Kerja/Ngajar/UBK/Tahun Akademik/2022-2023/Ganjil/Matkul/Algoritma dan Pemrograman/Learning-with-Python/Source"
paths = os.path.join(parrent, directory)
if os.path.isdir(paths):
    shutil.rmtree(paths)
    print(f"folder {directory} berhasil hapus")
else:
    print("tidak ada folder yang berhasil di hapus")