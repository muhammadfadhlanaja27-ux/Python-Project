# Class Induk
class Kendaraan:
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    # Getter
    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_harga(self, harga):
        if harga > 0:
            self.__harga = harga
        else:
            print("Harga tidak boleh nol atau negatif!")

    # Method untuk dioverride
    def deskripsi(self):
        return "Ini adalah kendaraan umum."


# Class Turunan Mobil
class Mobil(Kendaraan):
    def __init__(self, nama, harga, jumlah_pintu):
        super().__init__(nama, harga)
        self.jumlah_pintu = jumlah_pintu

    def deskripsi(self):
        return f"Mobil {self.get_nama()} dengan {self.jumlah_pintu} pintu."


# Class Turunan Motor
class Motor(Kendaraan):
    def __init__(self, nama, harga, jenis_motor):
        super().__init__(nama, harga)
        self.jenis_motor = jenis_motor

    def deskripsi(self):
        return f"Motor {self.get_nama()} jenis {self.jenis_motor}."


# Class Main Program
class MainProgram:
    def jalankan(self):
        print("=== Sistem Pendaftaran Kendaraan ===")
        print("1. Daftarkan Mobil")
        print("2. Daftarkan Motor")

        pilihan = input("Pilih jenis kendaraan (1/2): ")

        nama = input("Masukkan nama kendaraan: ")
        harga_input = input("Masukkan harga kendaraan: ")
        if not harga_input.isdigit():
            print("Harga harus berupa angka!")
            return
        harga = int(harga_input)

        if pilihan == "1":
            pintu_input = input("Masukkan jumlah pintu: ")
            if not pintu_input.isdigit():
                print("Jumlah pintu harus angka!")
                return
            pintu = int(pintu_input)
            kendaraan = Mobil(nama, harga, pintu)

        elif pilihan == "2":
            jenis = input("Masukkan jenis motor (matic/manual): ")
            kendaraan = Motor(nama, harga, jenis)

        else:
            print("Pilihan tidak valid!")
            return

        # Gunakan setter jika ingin ubah nama atau harga
        ubah_nama = input("Ingin ubah nama kendaraan? (y/n): ")
        if ubah_nama.lower() == 'y':
            nama_baru = input("Masukkan nama baru: ")
            kendaraan.set_nama(nama_baru)

        ubah_harga = input("Ingin ubah harga kendaraan? (y/n): ")
        if ubah_harga.lower() == 'y':
            harga_baru_input = input("Masukkan harga baru: ")
            if harga_baru_input.isdigit():
                kendaraan.set_harga(int(harga_baru_input))
            else:
                print("Harga baru tidak valid, tetap pakai harga lama.")

        # Output
        print("\n--- Info Kendaraan ---")
        print(kendaraan.deskripsi())
        print(f"Harga: Rp{kendaraan.get_harga():,}")

        # IF-ELSE logika pajak
        if kendaraan.get_harga() > 300_000_000:
            print("Status: Butuh Pajak Tinggi 🚨")
        else:
            print("Status: Pajak Normal ✅")


# Menjalankan program
if __name__ == "__main__":
    program = MainProgram()
    program.jalankan()
