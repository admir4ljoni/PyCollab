from __future__ import annotations

from Tenaga_Layanan.Dokter.dokter import Dokter

class DokterSpesialis(Dokter):
    def __init__(self, nama: str, nomor_pegawai: str, biaya_khusus: int):
        super().__init__(nama, nomor_pegawai)
        self.biaya_khusus = biaya_khusus

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Pegawai: {self.nomor_pegawai}")
        print(f"Biaya Khusus: {self.biaya_khusus}")