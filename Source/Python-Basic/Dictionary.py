"""
* Dalam Python versi 3.7 Dictionary adalah kumpulan pasangan yang diurutkan berdasarkan 'Key: Value'
* Dalam dokumentasi Python 3 Operasi utama pada Dictionary adalah menyimpan nilai dengan beberapa
* kunci dan mengekstrak nilai yang diberikan kunci tersebut. Dimungkinkan juga untuk menghapus key:value dengan kunci del
* Dictionary merupakan kumpulan yang dibuat, dapat diubah dan tidak mungkin adanya duplikat
* Dictionary ditulis dengan kurawa dan memiliki kunci dan nilai.
* Dictionary juga tipe data yang mirip dengan array tetapi bekerja dengan key dan value
* Setiap nilai yang disimpan dapat diakses dengan menggunakan kunci yang merupakan jenis objek apapun seperti string, number, list dan sebagainya
"""

# * Contoh Dictionary
fikom = {
    "Dekan": "Alexius",
    "Kaprodi": "Fifto",
    "Dosen": "Joko"
    }

"""
* values()
* Method values() akan mendapatkan nilai dari Dictionary
"""
print(fikom.values())

"""
* keys()
* Method keys() akan mendapatkan kunci dari Dictionary
"""
print(fikom.keys())

"""
* items()
* Method items() akan mendapatkan item Dictionary dan akan mengembalikan (return) sebagai Tuple
"""
print(fikom.items())

# * Kita juga bisa menggunakan kedua Method secara bersamaan dengan sentuhan looping
for key, value in fikom.items():
    print(f"Key: {key} Value: {value}")

# * Akses Item mengacu kepada kunci dengan menambahkan tanda kurung siku
print(fikom["Dosen"])
print(f"Siapa Dosen yang Mengampu Mata Kuliah ALPRO? {fikom['Dosen']}")

# * Akses Item juga dapat menggunakan Method get()
print(fikom.get("Dekan"))
print(f"Siapa Dekan Fakultas Fikom saat ini? {fikom.get('Dekan')}")

# * Menambah item pada Dictionary
fikom["Mata_Kuliah"] = "PROGRAMMING"
print(fikom)

# * Optional kita juga dapat menambahkan item ke Dictionary dengan memanfaatkan Method setdefault()
# * setdefault() akan mengembalikan nilai key yang ditentukan, Jika key tidak ada: masukan key dengan value yang ditentukan
print("\nOptional Adding items with setdefault()")
print(fikom)
fikom.setdefault("Jumlah_Mhs", 50)
print(fikom)

# * update() = Kita bisa melakukan perubahan (update) pada Dictionary 
# * dengan menggunakan Method update()
# * UPDATE TO K-V
print("\n")
fikom["Mata_Kuliah"] = "ALPRO" # * mengubah nilai item mengacu pada nama key
print(fikom)
print(fikom["Mata_Kuliah"])

# * Ketika ingin menggunakan Method update() Argumen harus berupa Dictionary atau objek 
# * yang dapat diubah dengan pasangan key:value
print(fikom)
fikom.update({"Dosen": "Joko Saputro"})
print(fikom)
print(fikom["Dosen"])

"""
* Remove Items
* Ada beberapa Method yang digunakan untuk menghapus item dari Dictionary seperti :
* pop(), popitem(), clear(), del()
"""
# * pop() : Method pop() akan menghapus dan mengembalikan item berdasarkan kunci yang diberikan
print(f"\nBefore pop(): {fikom}")
print(fikom.pop("Dosen"))
print(f"After pop(): {fikom}")

# * popitem() : Method popitem() akan menghapus item yang dimasukan terakhir ke Dictionary
print(f"\nBefore popitem(): {fikom}")
print(fikom.popitem())
print(f"After popitem(): {fikom}")

# * clear() : Method clear() akan mengosongkan semua item di dalam Dictionary
print(f"\nBefore clear(): {fikom}")
fikom.clear()
print(f"After clear(): {fikom}")

# * del() : Method kunci del() akan menghapus item dengan nama kunci yang ditentukan
fikom = {
    "Dekan": "Alexius",
    "Kaprodi": "Fifto",
    "Dosen": "Joko"
    }
print(f"\nBefore: {fikom}")
del fikom["Kaprodi"]
print(f"After: {fikom}")

# * kata kunci del juga dapat digunakan untuk menghapus semua Dictionary
print(f"\nBefore: {fikom}")
# del fikom # * ini di aktifkan akan erorr
print(f"After: {fikom}") # * ini akan menyebabkan erorr karena fikom sudah tidak ada lagi makanya akan menghasilkan output name fikom is not defined

"""
* Pengulangan Dictionary menggunakan for loop
* Pengulangan Dictionary dapat dilakukan dengan Key or Value
"""
myDict = {
    "key1": 100,
    "key2": 200,
    "key3": 300,
    "key4": 400
}
print("\n")
print(myDict.keys())
print(myDict.values())
print(myDict.items())

# * nilai yang dikembalikan ada key
for x in myDict:
    print(x) # * cetak semua key dalam Dictionary satu per satu

for y in myDict:
    print(myDict[y]) # * cetak semua value dalam Dictionary satu per satu

# * optional kita juga dapat menggunakan Method keys() dan values()
for x in myDict.keys(): # * ini akan mengembalikan key Dictionary
    print(x)

for y in myDict.values(): # * ini akan mengembalikan value Dictionary
    print(y)

# * kita juga bisa melakukan perulangan dengan menggunakan Method items() untuk mengembalikan key dan value
for z in myDict.items():
    print(z)

"""
* Menyalin Dictionary 
* Menyalin sebuah Dictionary dapat dilakukan dengan memanfaatkan Method bawaan yakni copy() fungsi bawaan dict()
! ini cara menyalin Dictionary yang kurang tepat misal dict2 = dict1
"""
# * Membuat salinan dengan Method copy()
print("\nMembuat salinan dengan Method copy()")
myDict2 = myDict.copy()
print(myDict2)

# * Membuat salinan dengan Fungsi dict()
print("\nMembuat salinan dengan Fungsi dict()")
myDict2 = dict(fikom)
print(myDict2)

"""
* Check key or value in a Dictionary
"""
print("\nCheck Key or Value in a Dictionary")
print(fikom)
print(myDict)

print("Dekan" in fikom.keys())
print("Mahasiswa" in fikom.keys())
print("Alexius" in fikom.values())
print(300 in myDict.values())

# * Kita juga dapat Menggabungkan 2 Dictionary
print("\nMerge Two Dictionary")
dict_a = {"a": 10, "b": 20}
dict_b = {"c": 30, "d": 40}
dict_c = {**dict_a, **dict_b} # * cara dengan menggunakan **kwargs in python
dict_d = dict_a | dict_b # * cara dengan menggunakan operator OR "|" Last Update Python 3.9+
print(dict_c)
print(dict_d)

"""
* Dalam Dictionary juga dimungkinkan untuk Dictionary Bersarang
"""
myFamily = {
    "anak1" : {
        "nama": "Emil",
        "umur": 35
    },
    "anak2": {
        "nama": "Sarah",
        "umur": 27
    },
    "anak3": {
        "nama": "Lius",
        "umur": 20
    }
}
print("\nNested Dictionaries")
print(myFamily["anak2"])
print(myFamily["anak2"]["umur"])
print(f"Berapakah umur Luis?: {myFamily['anak3']['umur']} tahun")

# * Optional misa kita memiliki 3 Dictionary yang akan kita gabungkan ke 1 Dictionary
print("\n")
anak1 = {
    "nama": "Emil",
    "umur": 35
}
anak2 = {
    "nama": "Sarah",
    "umur": 27
}
anak3 = {
    "nama": "Lius",
    "umur": 20
}

myFamily2 = {
    "anak1": anak1,
    "anak2": anak2,
    "anak3": anak3
}
print(myFamily2)

# * Extract Nilai Dictionary sebagai List
print("\nExtract Dictionary Value as a List")
myDict = {"A": 300, "B": 400, "C": 150, "D": 200, "E": 100}
myList = list(myDict.values()) # * Menggunakan fungsi list()
print(myList)
print(type(myList))

print("\n")
my_list = [i for i in myDict.values()] # * menggunakan list comprehension
print(my_list)

print("\n")
my_list1 = []
for i in myDict.values():
    my_list1.append(i)

print(my_list1)

# * Extract Nilai Dictionary sebagai List dan List
print("\nExtract Dictionary Value as a List of List")
myDict = {"A": [300, 200, 150], "B": [110, 120, 130], "C": [210, 220, 230]}
print(myDict)
my_list = list(myDict.values())
print(my_list)
print(my_list[0])
print(my_list[:3])
nilai = myDict["B"]
print(f"Nilai kamu adalah: {nilai[1]}")




# TODO 1 : Coding Exercise Check-in: Python Dictionaries
# ? TASK: Add the key-value pair "key5", 500 to the dictionary defined below, then print all key-value pairs of the updated dictionary.
myDict = {
    "key1": 100,
    "key2": 200,
    "key3": 300,
    "key4": 400
}
# * Your Code Goes Here

# TODO 2 : Coding Exercise Check-in: Python Dictionaries
# ? Add "Jhon" to the phonebook with the phone number 8127882119, and remove Jake from the phonebook
phonebook = {
    "Anies": 8127888812,
    "Jack": 8127898129,
    "Jake": 8127782192
}
# * Your Code Goes Here
phonebook["Jhon"] = 8127882119  
del phonebook["Jake"] 

# * Testing Code
if "Jhon" in phonebook and "Jake" not in phonebook:
    print("Jhon is listed in the phonebook.")
    print("Jake is not listed in the phonebook")
else:
    print("Incorrect Answer")
