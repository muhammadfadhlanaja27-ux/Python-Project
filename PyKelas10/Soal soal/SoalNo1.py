class Hewan:
    def bersuara(self):
        # method bersuara() di kelas induk
        print("Suara Hewan")

class Kucing(Hewan):
    def bersuara(self):
        # method bersuara() ditulis ulang (override) di kelas Kucing
        print("Meong")

class Anjing(Hewan):
    # method bersuara() ditulis ulang (override) di kelas Anjing
    def bersuara(self):
        print("Guk")

kucing = Kucing()
anjing = Anjing()
hewan = Hewan()

# memanggil method bersuara() masing-masing objek
kucing.bersuara()
anjing.bersuara()
hewan.bersuara()
