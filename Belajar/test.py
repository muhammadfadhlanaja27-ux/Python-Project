import random

print("Pilih angka antara 1 sampai 10:")

angka_rahasia = random.randint(1, 10)
tebakan = None 
while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakan Anda: "))
    if tebakan < angka_rahasia:
        print("Terlalu rendah! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu tinggi! Coba lagi.")
    else:
        print("Selamat! Tebakan Anda benar.")
print("Terima kasih telah bermain!")
