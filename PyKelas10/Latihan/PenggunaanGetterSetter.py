class Produk:
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga

    def set_nama(self, nama_baru):
        self._nama = nama_baru

    def get_nama(self):
        return self._nama

    def get_harga(self):
        return self._harga

    def set_harga(self, harga_baru):
        if harga_baru > 0:
          self._harga = harga_baru
        else:
          print("Harga harus lebih dari 0")

produk1 = Produk("Laptop",5000000)

print("Nama produk:", produk1.get_nama())
print("Harga produk:", produk1.get_harga())

produk1.set_nama("Laptop Gaming")
produk1.set_harga(6500000)

print("Nama produk baru:", produk1.get_nama())
print("Harga produk baru:", produk1.get_harga())

produk1.set_harga(-10000)
print("Harga setelah input tidak valid:", produk1.get_harga())
