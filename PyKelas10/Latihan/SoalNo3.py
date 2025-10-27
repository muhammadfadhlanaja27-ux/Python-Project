class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Hewan mengeluarkan suara")

class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} berkata Meong")

class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama} berkata Guk-guk")

# Daftar objek hewan
daftar_hewan = [
    Kucing("Kitty"),
    Anjing("Bruno"),
    Hewan("Umum")
]

for h in daftar_hewan:
    h.bersuara()
