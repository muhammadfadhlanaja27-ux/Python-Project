class Member:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.simpanan = 0

class Simpan:
    def simpan_uang(self, jumlah, member):
        member.simpanan += jumlah
        print(f"{member.nama} menyimpan Rp{jumlah:,}")

class Pinjam:
    def pinjam_uang(self, jumlah, member):
        if jumlah <= member.simpanan:
            member.simpanan -= jumlah
            print(f"{member.nama} meminjam Rp{jumlah:,}")
        else:
            print("Pinjaman gagal, saldo tidak mencukupi.")

class Daftar(Member):
    def __init__(self, nama, alamat):
        super().__init__(nama, alamat)

class Transaksi(Simpan, Pinjam):
    def __init__(self, member):
        self.member = member

    def transaksi_simpan(self, jumlah):
        self.simpan_uang(jumlah, self.member)

    def transaksi_pinjam(self, jumlah):
        self.pinjam_uang(jumlah, self.member)

    def lihat_saldo(self):
        print(f"Sisa saldo {self.member.nama}: Rp{self.member.simpanan:,}")


# Program utama
member = None
transaksi = None

while True:
    print("\n<===MENU===>\n1. Daftar\n2. Simpan\n3. Pinjam\n4. Lihat Saldo\n5. Keluar")
    pilih = input("\nPilih: ")

    if pilih == "1":
        if not member:
            n = input("Nama: ")
            a = input("Alamat: ")
            member = Daftar(n, a)
            transaksi = Transaksi(member)
            print(f"Member {member.nama} berhasil didaftarkan.")
        else:
            print("Sudah terdaftar.")

    elif pilih == "2" and member:
        jumlah = int(input("Jumlah simpanan: "))
        transaksi.transaksi_simpan(jumlah)

    elif pilih == "3" and member:
        jumlah = int(input("Jumlah pinjaman: "))
        transaksi.transaksi_pinjam(jumlah)

    elif pilih == "4" and member:
        transaksi.lihat_saldo()

    elif pilih == "5":
        print("Terima kasih.")
        break

    else:
        print("Silakan daftar dulu.") if not member else print("Pilihan tidak valid.")
