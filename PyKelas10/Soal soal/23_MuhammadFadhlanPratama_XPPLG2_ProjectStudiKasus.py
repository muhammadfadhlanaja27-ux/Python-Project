class Member:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

class Simpan:
    def __init__(self):
        self.simpanan = 0

    def simpan_uang(self, jumlah):
        self.simpanan += jumlah
        print(f"Simpanan berhasil. Jumlah total simpanan: {self.simpanan}")

class Pinjam:
    def __init__(self):
        self.pinjaman = 0

    def pinjam_uang(self, jumlah):
        self.pinjaman += jumlah
        print(f"Pinjaman berhasil. Jumlah total pinjaman: {self.pinjaman}")

class Daftar(Member):
    def __init__(self):
        nama = input("Masukkan nama member: ")
        alamat = input("Masukkan alamat member: ")
        super().__init__(nama, alamat)
        print(f"Member '{self.nama}' berhasil didaftarkan.\n")

class Transaksi(Simpan, Pinjam):
    def __init__(self):
        Simpan.__init__(self)
        Pinjam.__init__(self)

    def menu(self, nama):
        while True:
            print(f"\n--- MENU TRANSAKSI untuk {nama} ---")
            print("1. Simpan Uang")
            print("2. Pinjam Uang")
            print("3. Kembali ke menu utama")
            pilihan = input("Pilih (1/2/3): ")

            if pilihan == '1':
                jumlah = int(input("Masukkan jumlah simpanan: "))
                self.simpan_uang(jumlah)
            elif pilihan == '2':
                jumlah = int(input("Masukkan jumlah pinjaman: "))
                self.pinjam_uang(jumlah)
            elif pilihan == '3':
                break
            else:
                print("Pilihan tidak valid.")

daftar_member = {}

while True:
    print("\n===== MENU UTAMA =====")
    print("1. Daftar Member Baru")
    print("2. Transaksi")
    print("3. Lihat Daftar Member")
    print("4. Keluar")

    pilih = input("Pilih menu (1/2/3/4): ")

    if pilih == '1':
        member_baru = Daftar()
        transaksi_baru = Transaksi()
        daftar_member[member_baru.nama] = {"data": member_baru, "transaksi": transaksi_baru}

    elif pilih == '2':
        if not daftar_member:
            print("Belum ada member. Silakan daftar dulu.")
            continue

        nama = input("Masukkan nama member untuk transaksi: ")
        if nama in daftar_member:
            daftar_member[nama]["transaksi"].menu(nama)
        else:
            print("Member tidak ditemukan.")

    elif pilih == '3':
        if not daftar_member:
            print("Belum ada member terdaftar.")
        else:
            print("\n--- Daftar Member ---")
            for m in daftar_member:
                print(f"- {m} (Alamat: {daftar_member[m]['data'].alamat})")

    elif pilih == '4':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
