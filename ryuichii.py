from prettytable import PrettyTable
from datetime import datetime

# Menampilkan header aplikasi
print("=" * 100)
print("Aplikasi Penghitung Jumlah Biaya PT Ryuichii")
print("=" * 100)

# Input nama pegawai
author = input("Nama Pegawai: ")

# Inisialisasi list untuk menyimpan data barang
darat = []
ulang = 0

# Input jumlah barang
jml = int(input("Jumlah barang yang mau di input: "))
print("="*100)
print("inputan barang")
print("")

# Input data barang
while ulang < jml:
    print(f"Masukkan data untuk Barang ke-{ulang + 1}")
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
    print(f"Tanggal dan Waktu Input: {current_time}")
    input1 = input("Nama Barang: ")
    input2 = int(input("Jumlah barang: "))
    input3 = int(input("Harga barang: "))

    # Hitung diskon jika harga barang >= 100000
    if input3 >= 100000:
        diskon = input3 * 5 / 100  # Diskon 5% jika harga >= 100000
    else:
        diskon = 0  # Tidak ada diskon jika harga < 100000

    # Hitung total harga sebelum diskon
    total_harga = input2 * input3

    # Hitung total harga setelah diskon
    harga_setelah_diskon = total_harga - diskon

    # Simpan data barang ke list
    darat.append((input1, input2, input3, diskon, harga_setelah_diskon,current_time))
    ulang += 1

# Menampilkan hasil dalam bentuk tabel
table = PrettyTable()
table.field_names = ["No", "Nama Barang", "Jumlah Barang", "Harga Barang", "Diskon", "Total Harga Setelah Diskon","waktu"]

# Menambahkan data ke tabel
for i, mk in enumerate(darat, start=1):
    table.add_row([i, mk[0], mk[1], mk[2], mk[3], mk[4],mk[5]])

# Menampilkan informasi rekap
print(f"Nilai rekap dari: {author}")
print(table)

# Menghitung total keseluruhan setelah diskon
total_akhir = sum(mk[4] for mk in darat)
print(f"Total keseluruhan setelah diskon: Rp {total_akhir:,.2f}")
