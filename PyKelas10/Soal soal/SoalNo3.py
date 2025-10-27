class Burung:
    def terbang(self):  # method terbang() pada class burung
        print("Burung terbang di langit")

class Pesawat:
    def terbang(self):  # method terbang() pada class pesawat
        print("Pesawat terbang di udara")

def coba_terbang(objek):
    objek.terbang()

burung = Burung()
pesawat = Pesawat()

coba_terbang(burung)   # memanggil fungsi coba_terbang dengan objek burung
coba_terbang(pesawat)  # memanggil fungsi coba_terbang dengan objek pesawat
