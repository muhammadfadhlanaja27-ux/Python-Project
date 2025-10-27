#class induk
class Buku:
    def __init__(self, judul):
        self.judul = judul

    def deskripsi(self):
        print(f"Buku: {self.judul}")

#class turunan
class BukuFiksi(Buku):
    def deskripsi(self): #overriding method dari class induk
        print(f"Buku Fiksi: {self.judul}")

class BukuNonFiksi(Buku):
    def deskripsi(self): #overriding method dari class induk
        print(f"Buku Non-Fiksi: {self.judul}")

#membuat list berisi objek buku dari class turunan
daftar_buku = [
    BukuFiksi("Harry Potter"),
    BukuNonFiksi("Ensiklopedia Sains"),
    BukuFiksi("Lord of the Rings"),
    BukuNonFiksi("Sejarah Dunia")
]

#pemanggil deskripsi() untuk setiap objek dalam daftar_buku
for buku in daftar_buku:
    buku.deskripsi() #memanggil method deskripsi() sesuai class masing-masing
-