# Kelas induk
class BangunDatar:
    def luas(self):
        print("Menghitung luas bangun datar")

# Kelas turunan dengan method overriding
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    # Method overriding ⇒ menimpa method luas() di BangunDatar
    def luas(self):
        print(f"Luas persegi: {self.sisi * self.sisi}")

# Kelas turunan lain dengan method overriding
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        print(f"Luas persegi panjang: {self.panjang * self.lebar}")

# Contoh method overloading (simulasi) pakai *args
class Kalkulator:
    def tambah(self, *args):
        hasil = sum(args)
        print(f"Hasil penjumlahan: {hasil}")

# Membuat objek
bangun = BangunDatar()
persegi = Persegi(4)
persegi_panjang = PersegiPanjang(5, 3)
kalkulator = Kalkulator()

# Polimorfisme dengan inheritance & overriding
daftar_bangun = [bangun, persegi, persegi_panjang]
for b in daftar_bangun:
    b.luas()

# Simulasi method overloading
kalkulator.tambah(2, 3)
kalkulator.tambah(2, 3, 4)
kalkulator.tambah(1, 2, 3, 4, 5)
