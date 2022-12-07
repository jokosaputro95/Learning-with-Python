"""
* Tipe data adalah suatu media atau memori pada komputer yang digunakan 
* untuk menampung informasi.
* Tipe data pada Python :
* - Boolean : True atau False
* - String : diinisialisasi pada karakter, huruf, angka dll yang di apit oleh 
* tanda kutip tunggal atau ganda '' or ""
* - Integer : bilangan bulat
* - Float : bilangan memiliki koma
* - Hexadecimal : bilangan dalam format heksa (bilangan berbasis 16)
* - Complex : Pasangan angka real dan imajiner
* - List : Data untaian yang menyimpan berbagai tipe data tetapi isinya tidak bisa diubah (immutable)
* - Tuple : Data untaian yang menyimpan berbagai tipe data tetapi isinya tidak bisa diubah (immutable)
* - Dictionary : Data untaian yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai
"""
# tipe data Boolean
print(True)
print(False)

# tipe data String
print('welcome')
print("welcome to Python!")

# tipe data Integer
print(20)

# tipe data Float
print(3.14)

# tipe data Hexadecimal
print(hex(400))

# tipe data Complex
print(5j)

# tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])
print(["satu", 2, "tiga", 4, "lima"])

# tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

# tipe data Dictionary
print({"nama":"Budi", 'umur':20})
# tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Andi", 'umur':21} # proses inisialisasi variabel biodata
print(biodata) # proses pencetakan variabel biodata yang berisi tipe data Dictionary
print(type(biodata)) # * fungsi type untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe data dictionary

"""
* Format pendeklrasian variabel : NamaVariabel = IsiVariabel
* Aturan pendeklrasian variabel dalam Python:
* 1. Penulisan variabel diawali dengan huruf (a-z, A-Z) atau diawali dengan underscore (_)
* 2. Karakter selanjutnya dapat berupa huruf, garis bawah/underscore _ atau angka
* 3. Nama variabel bersifat sensitif (case-sensitif) Artinya huruf kecil dan huruf besar dibedakan
* - contoh : namaDepan dan namadepan ini adalah variabel yang berbeda.
* 4. untuk menetapkan nilai ke dalam variabel dapat menggunakan tanda sama dengan (=), ini juga dikenal sebagai operator penugasan (assignment)
"""
print("\nVariables, Arithmethic with Numbers")
print(1 + 1)
print(20 - 5)
print(20 * 20)
print(20 / 2)
print(2 ** 3)
print((2 + 2) * (10 - 5))

# proses memasukan data ke dalam variabel
nilai_belanja = 50000
tarif_pajak = 0.11

nilai_pajak = nilai_belanja * tarif_pajak
print(nilai_pajak)
sub_total = nilai_belanja + nilai_pajak
print(sub_total)
jml_total = nilai_belanja + (nilai_belanja * tarif_pajak)
print(jml_total)
print(type(jml_total))