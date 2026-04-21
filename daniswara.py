class Karyawan:
    def __init__(self, nama, gaji, skor_kinerja):
        if skor_kinerja < 0 or skor_kinerja > 100:
            raise ValueError("Skor kinerja harus antara 0 dan 100")

        self.nama = nama
        self.gaji = gaji
        self.skor_kinerja = skor_kinerja

    def hitung_bonus(self):
        return "Bonus tidak ada"
    

class KaryawanTetap(Karyawan):
    def hitung_bonus(self):
        return 0.2 * self.gaji if self.skor_kinerja >= 80 else super().hitung_bonus()


class KaryawanKontrak(Karyawan):
    def hitung_bonus(self):
        return 0.1 * self.gaji if self.skor_kinerja >= 85 else super().hitung_bonus()

class KaryawanFreelance(Karyawan):
    def hitung_bonus(self):
        return 500000 if self.skor_kinerja >= 90 else super().hitung_bonus()

def proses_bonus(daftar_karyawan):
    for karyawan in daftar_karyawan:
        print(f"Nama: {karyawan.nama}\nGaji Pokok: {karyawan.gaji}\nBonus: {karyawan.hitung_bonus()}\nSkor Kinerja: {karyawan.skor_kinerja}")
        print("=" * 30)
    
daftar = [
    KaryawanTetap("Jono 1", 8000000, 85),
    KaryawanKontrak("Jono 2", 6000000, 80),
    KaryawanFreelance("Jono 3", 0, 92)
]

proses_bonus(daftar)