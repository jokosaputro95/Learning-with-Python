"""
* Python memungkinkan pengguna untuk melakukan interaksi input
* untuk dapat melakukan input pengguna kita bisa menggunakan Method input()
* Dalam bahasa Python fungsi / method input() akan mengembalikan keluaran dalam bentuk String.
* Meskipun yang diinputkan berupa number dibalik layar proses input data tersebut berbentuk String
* jika kita ingin mendapatkan hasilnya bertipe data lain seperti integer atau float maka kita dapat mengkombinasikan
* -> fungsi / method input() dengan fungsi int() atau dengan fungsi float()
"""

# * Input User
print("Input User Output String")
phonebook = input("Enter your number phone: ")
print(phonebook)
print("Tipe data dari varibel phonebook adalah:", type(phonebook))

# * Get Integer Output
print("\nInput User Output Integer")
phonebook = int(input("Enter your number phone: "))
print(phonebook)
print(f"Tipe data dari varibel phonebook adalah: {type(phonebook)}")

# * Get Float Output
print("\nInput User Output Float")
phonebook = float(input("Enter your number float: "))
print(phonebook)
print(f"Tipe data dari varibel phonebook adalah: {type(phonebook)}")

# TODO 1 : Coding Exercise Check-in: Python User Input
# ? TASK : Buatlah program yang dapat menghitung kecepatan dan waktu tempuh suatu mobil
# ? -> dengan detail sebagai berikut:
# ? * variabel : kecepatan, waktu, dan jarak
# ? * output : Kecepatan rata-rata(km/jam)  : <kecepatan>
# ? * output : Waktu tempuh (jam)           : <waktu>
# ? * output : Jarak tempuh                 : <kecepatan> * <waktu> = <jarak> km

# * Your Code Goes Here
print("\n============= DATA KECEPATAN MOBIL =============")
kecepatan = int(input("Masukan kecepatan rata-rata (km/jam): "))
waktu = int(input("Masukan watku tempuh (jam): "))
jarak = kecepatan * waktu

print(f"Kecepatan rata-rata (km/jam): {kecepatan}")
print(f"Waktu tempuh (jam): {waktu}")
print(f"Jarak tempuh: {jarak} km")

# TODO 2 : Coding Exercise Check-in: Python User Input
# ? Sebuah operator "XYZ" paca bayar menerapkan tarif service sebegai berikut:
# ? - Percakapan = Rp. 1000/menit, 
# ? - SMS = Rp. 300/sms, 
# ? - Abodemen = Rp. 20000/bulan
# ? TASK : Buatlah program menghitung besar tagihan telepon dengan Input:
# ? * variabel : nama, percakapan, SMS
# ? Title : DATA PELANGGAN
# ? * output : Nama Pelanggan   : <nama>
# ? * output : Percakapan       : <cakap> menit
# ? * output : SMS              : <sms> kali
# ? TITLE : TAGIHAN
# ? * output : Abodemen         : <abn>
# ? * output : Biaya Percakapan : <rp_cakap>
# ? * output : Biaya SMS        : <rp_sms>
# ? * output : Total Tagihan    : <t_tagih>

# * Your Code Goes Here
print("\n============= PROGRAM MENGHITUNG TAGIHAN TELEPON =============")
service = {
    "percakapan": 1000,
    "SMS" : 300,
    "abn": 20000
}

nama = input("Masukkan Nama Pelanggan: ")
cakap = int(input("Masukkan Jumlah Percakapan (menit): "))
sms = int(input("Masukkan Jumlah SMS (kali): "))

rp_cakap = cakap * service["percakapan"]
rp_sms = sms * service["SMS"]
t_tagih = service["abn"] + rp_cakap + rp_sms

print("\nDATA PELANGGAN")
print(f"Nama Pelanggan      : {nama}")
print(f"Percakapan          : {cakap} menit")
print(f"SMS                 : {sms} kali")

print("\nTAGIHAN")
print(f"Abodemen            : Rp. {service['abn']}")
print(f"Biaya percakapan    : Rp. {rp_cakap}")
print(f"Biaya SMS           : Rp. {rp_sms}")
print(f"Total tagihan       : Rp. {t_tagih}")