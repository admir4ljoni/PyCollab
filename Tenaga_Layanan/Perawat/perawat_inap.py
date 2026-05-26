from __future__ import annotations
from Tenaga_Layanan.Perawat.perawat import Perawat

class PerawatInap(Perawat):
    def __init__(self, nama: str, nomor_pegawai: str, biaya_per_malam: int):
        if not isinstance(biaya_per_malam, int):
            raise TypeError("Biaya per malam harus berupa integer")
        if biaya_per_malam < 0:
            raise ValueError("Biaya per malam tidak boleh negatif")

        super().__init__(nama, nomor_pegawai)

        self.biaya_per_malam = biaya_per_malam

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Pegawai: {self.nomor_pegawai}")
        print(f"Biaya Per Malam: {self.biaya_per_malam}")
