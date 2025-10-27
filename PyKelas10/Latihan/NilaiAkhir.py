class Siswa:
    def __init__(self, nama):
        self.__nama = nama
        self.__nilai_tugas = 0
        self.__nilai_ujian = 0
        self.__nilai_akhir = 0

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def set_nilai_tugas(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai_tugas = nilai
            self.hitung_nilai_akhir()
        else:
            print("Nilai tugas harus antara 0 dan 100.")

    def get_nilai_tugas(self):
        return self.__nilai_tugas

    def set_nilai_ujian(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai_ujian = nilai
            self.hitung_nilai_akhir()
        else:
            print("Nilai ujian harus antara 0 dan 100.")

    def get_nilai_ujian(self):
        return self.__nilai_ujian

    def get_nilai_akhir(self):
        return round(self.__nilai_akhir, 2)

    def hitung_nilai_akhir(self):
        self.__nilai_akhir = 0.4 * self.__nilai_tugas + 0.6 * self.__nilai_ujian

    def status_lulus(self):
        return "Lulus" if self.__nilai_akhir >= 75 else "Tidak Lulus"

siswal = Siswa("Nadila")
siswal.set_nilai_tugas(80)
siswal.set_nilai_ujian(75)

print("Nama:", siswal.get_nama())
print("Nilai Tugas:", siswal.get_nilai_tugas())
print("Nilai Ujian:", siswal.get_nilai_ujian())
print("Nilai Akhir:", siswal.get_nilai_akhir())
print("Status:", siswal.status_lulus())

siswal.set_nilai_ujian(110)
