class Kalkulator:
    def __init__(self):
        self.__bilangan1 = 0
        self.__bilangan2 = 0

    # Setter
    def set_bilangan1(self, nilai):
        self.__bilangan1 = nilai

    def set_bilangan2(self, nilai):
        self.__bilangan2 = nilai

    # Getter
    def get_bilangan1(self):
        return self.__bilangan1

    def get_bilangan2(self):
        return self.__bilangan2

    # Method dasar yang akan dioverride
    def konversi(self):
        raise NotImplementedError("Method konversi() harus dioverride di class turunan.")


class KalkulatorPenjumlahan(Kalkulator):
    def konversi(self):
        return self.get_bilangan1() + self.get_bilangan2()


class KalkulatorPengurangan(Kalkulator):
    def konversi(self):
        return self.get_bilangan1() - self.get_bilangan2()


class MainProgram:
    def jalankan(self):
        print("=== Program Kalkulator Sederhana ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")

        pilihan = input("Pilih operasi (1/2): ")

        try:
            bil1 = float(input("Masukkan bilangan pertama: "))
            bil2 = float(input("Masukkan bilangan kedua: "))
        except ValueError:
            print("Input harus berupa angka.")
            return

        if pilihan == '1':
            kalkulator = KalkulatorPenjumlahan()
        elif pilihan == '2':
            kalkulator = KalkulatorPengurangan()
        else:
            print("Pilihan tidak valid.")
            return

        kalkulator.set_bilangan1(bil1)
        kalkulator.set_bilangan2(bil2)

        hasil = kalkulator.konversi()
        print(f"Hasil perhitungan: {hasil}")


# Jalankan program
if __name__ == "__main__":
    program = MainProgram()
    program.jalankan()
