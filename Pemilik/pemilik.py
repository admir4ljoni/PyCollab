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
        pass

    def tampilkan_hewan_peliharaan_berdasarkan_jenis(
        self,
        jenis_hewan: type
    ):
        pass