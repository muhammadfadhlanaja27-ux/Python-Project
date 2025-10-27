# Class Induk
class Produk:
    # Konstruktor untuk inisialisasi atribut nama, harga, dan jumlah
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    # Method untuk menghitung total harga tanpa pajak/diskon
    def hitung_total(self):
        return self.harga * self.jumlah


# Class Turunan Buku (mewarisi dari Produk)
class Buku(Produk):
    def hitung_total(self):
        return super().hitung_total()


# Class Turunan Elektronik
class Elektronik(Produk):
    # Overriding method hitung_total untuk menambahkan pajak
    def hitung_total(self):
        pajak = 0.1 * (self.harga * self.jumlah)  # hitung pajak 10%
        return super().hitung_total() + pajak


# Class Turunan Pakaian (mewarisi dari Produk)
class Pakaian(Produk):
    # Overriding method hitung_total untuk menerapkan diskon jika beli > 3
    def hitung_total(self):
        total = self.harga * self.jumlah  # hitung total awal
        if self.jumlah > 3:  # jika jumlah lebih dari 3
            diskon = 0.2 * total  # total hitung diskon 20%
            total -= diskon  # kurangi diskon dari total
        return total  # kembalikan total akhir setelah diskon (jika ada)


# List Belanja dari berbagai class turunan
daftar_belanja = [
    Buku("Python Dasar", 100000, 2),
    Elektronik("Headset", 250000, 1),
    Pakaian("Kaos Polos", 50000, 5)
]

# Ringkasan Pembelian
print("=== Ringkasan Pembelian ===")
total_akhir = 0

# Perulangan untuk setiap produk di dalam daftar belanja
for produk in daftar_belanja:
    subtotal = produk.hitung_total()
    print(f"{produk.nama} - Total: Rp{subtotal:,.0f}")
    total_akhir += subtotal

# Cetak total seluruh belanja setelah perulangan selesai
print(f"\nTotal Seluruh Pembelian: Rp{total_akhir:,.0f}")
