from __future__ import annotations

from Tenaga_Layanan.Dokter.dokter import Dokter

class DokterUmum(Dokter):
    def __init__(self, nama: str, nomor_pegawai: str):
        super().__init__(nama, nomor_pegawai)

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Pegawai: {self.nomor_pegawai}")