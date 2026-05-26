from __future__ import annotations

class PerawatGrooming(Perawat):
    def __init__(self, nama: str, nomor_pegawai: str):
        super().__init__(nama, nomor_pegawai)

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Pegawai: {self.nomor_pegawai}")
        print(f"Biaya Per Malam: {self.biaya_per_malam}")
