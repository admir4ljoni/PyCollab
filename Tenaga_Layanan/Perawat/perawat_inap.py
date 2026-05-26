from __future__ import annotations

class PerawatInap(Perawat):
    def __init__(self, nama: str, nomor_pegawai: str, biaya_per_malam: int):
        super().__init__(nama, nomor_pegawai)

        if not isinstance(biaya_per_malam, int):
            raise TypeError("Biaya per malam harus berupa integer")
        if biaya_per_malam < 0:
            raise ValueError("Biaya per malam tidak boleh negatif")

        self.biaya_per_malam = biaya_per_malam