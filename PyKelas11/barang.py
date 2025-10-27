hargaA = 50000
hargaB = 75000

print("Harga Barang A Rp 50.000")
print("Harga Barang B Rp 75.000")
jumlahA = int(input("Masukan Jumlah barang A : "))
jumlahB = int(input("Masukan Jumlah barang B : "))
total = (hargaA * jumlahA)+(hargaB * jumlahB)
if total >= 200000 :
  diskon = total * 0.10
  totalHarga = total - diskon
  print(f"Jadi Total Harga semua adalah : {totalHarga}")
else:
  print(f"Jadi Total Harga semua adalah : {total}")
