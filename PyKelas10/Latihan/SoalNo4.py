class Produk:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def hitung_total(self):
        return self.harga * self.jumlah

class Buku(Produk):
    def hitung_total(self):
        return super().hitung_total()

class Elektronik(Produk):
    def hitung_total(self):
        pajak = 0.1 * (self.harga * self.jumlah)
        return super().hitung_total() + pajak
      
class Pakaian(Produk):
    def hitung_total(self):
        total = self.harga * self.jumlah
        if self.jumlah > 3:
            diskon = 0.2 * total
            total -= diskon
        return total

daftar_belanja = [
    Buku("Python Dasar", 100000, 2),
    Elektronik("Headset", 250000, 1),
    Pakaian("Kaos Polos", 50000, 5)
]

print("=== Ringkasan Pembelian ===")
total_akhir = 0

for produk in daftar_belanja:
    subtotal = produk.hitung_total()
    print(f"{produk.nama} - Total: Rp{subtotal:,.0f}")
    total_akhir += subtotal

print(f"\nTotal Seluruh Pembelian: Rp{total_akhir:,.0f}")
