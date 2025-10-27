#super class
class KonversiMataUang:
    def __init__(self, jumlah):
        self.__jumlah = jumlah
        self.__hasil = 0

    def get_jumlah(self):
        return self.__jumlah

    def get_hasil(self):
        return self.__hasil

    def set_jumlah(self, jumlah):
        self.__jumlah = jumlah

    def set_hasil(self, hasil):
        self.__hasil = hasil

    def info(self):
        return "ini adalah method class induk konversi mata uang"

#subclass
class IDRkeUSD(KonversiMataUang):
    def __init__(self, jumlah):
        super().__init__(jumlah)

    def konversi(self):
        return self.get_jumlah() / 15000

    def info(self):
        return "ini adalah konversi IDR to USD"

#subclass
class USDkeIDR(KonversiMataUang):
    def __init__(self, jumlah):
        super().__init__(jumlah)

    def konversi(self):
        return self.get_jumlah() * 15000

    def info(self):
        return "ini adalah konversi USD ke IDR"

#class program
class Mainprogram:
    def jalankan(self):
        while True:
            print("\nProgram Konversi Uang")
            print("1. IDR ke USD")
            print("2. USD ke IDR")
            pilihan = input("Masukan angka pilihan anda : ")

            if pilihan == '1':
                print("Ini Konversi IDR ke USD")
                jumlah = int(input("Masukan jumlah mata uang IDR : "))
                konvert = IDRkeUSD(jumlah)
                hasil = konvert.konversi()
                print(f"Hasil Konversi : {hasil:.2f} USD")
            elif pilihan == '2':
                print("Ini konversi USD ke IDR")
                jumlah = int(input("Masukan jumlah mata uang USD : "))
                konvert = USDkeIDR(jumlah)
                hasil = konvert.konversi()
                print(f"Hasil Konversi : {hasil:.2f} IDR")
            else:
                print("Pilihan tidak ada")

            pengulangan = input("Apakah anda ingin mengulang kembali? (y/n) : ")
            if pengulangan.lower() != 'y':
                print("Terimakasih telah menggunakan program ini...")
                break

#pemanggilan class Mainprogram
if __name__ == "__main__":
    program = Mainprogram()
    program.jalankan()