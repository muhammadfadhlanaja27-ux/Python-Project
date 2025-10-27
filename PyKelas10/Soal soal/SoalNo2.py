class Hitung:
    # menggunakan *args untuk menerima banyak argumen
    def tambah(self, *args):
        hasil = sum(args)  # menjumlahkan semua nilai dalam args
        print(f"Hasil: {hasil}")  # menampilkan hasil penjumlahan

h = Hitung()
h.tambah(2, 3)           # memanggil method tambah() dengan 2 angka
h.tambah(1, 2, 3, 4, 5)  # memanggil method tambah() dengan 5 angka
