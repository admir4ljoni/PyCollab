class Pemilik:
    def __init__(
        self,
        nama: str,
        narahubung: str,
    ):
        self.nama = nama
        self.narahubung = narahubung

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Narahubung: {self.narahubung}")

    def tampilkan_hewan_peliharaan(self):
        from Hewan.hewan import Hewan
        Hewan.tampilkan_hewan_berdasarkan_jenis_atau_pemilik(pemilik=self)

    def tampilkan_hewan_peliharaan_berdasarkan_jenis(
        self,
        jenis_hewan: type
    ):
        from Hewan.hewan import Hewan
        Hewan.tampilkan_hewan_berdasarkan_jenis_atau_pemilik(jenis_hewan=jenis_hewan, pemilik=self)
        