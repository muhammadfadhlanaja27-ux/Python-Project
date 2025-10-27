class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def lembur(self, jam=None):
        if jam is None:
            print(f"{self.nama} melakukan lembur standar selama 2 jam.")
        else:
            print(f"{self.nama} melakukan lembur selama {jam} jam.")

class Manager(Karyawan):
    def __init__(self, nama, gaji):
        super().__init__(nama, gaji)

    def tugas(self):
        print(f"{self.nama} bertugas mengatur tim.")

class Staff(Karyawan):
    def __init__(self, nama, gaji):
        super().__init__(nama, gaji)

    def tugas(self):
        print(f"{self.nama} bertugas menyelesaikan pekerjaan harian.")

mgr = Manager("Ashep", 15000000)
stf = Staff("Icha", 20000000)

print("<=== MANAGER ===>")
mgr.tugas()
mgr.lembur()
mgr.lembur(5)

print("\n<=== STAFF ===>")
stf.tugas()
stf.lembur()
stf.lembur(3)
