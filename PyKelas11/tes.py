'''total = 275000

sr = total // 100000
sisauang = total % 100000
total = sisauang

lm = total // 50000
sisauang = total % 50000
total = sisauang

da = total // 20000
sisauang = total % 20000
total = sisauang

lr = total // 5000
sisauang = total % 5000
total = sisauang

print(f"100000 = {sr}")
print(f"50000 = {lm}")
print(f"20000 = {da}")
print(f"5000 = {lr}")'''


# Mulai program
total = 275000
pecahan = [100000, 50000, 20000, 5000]

for nilai in pecahan:
    jumlah_lembar = total // nilai
    total = total % nilai
    print(f"{nilai} = {jumlah_lembar}")
# Selesai


awal = int(input("Masukan angka : "))
akhir = int(input("Masukan angka : "))

for i in range (awal, akhir +1 ):
  if i % 2 == 0:
    print(i,end=" ")