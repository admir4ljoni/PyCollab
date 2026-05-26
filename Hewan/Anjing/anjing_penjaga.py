from __future__ import annotations

from Hewan.Anjing.anjing import Anjing

class AnjingPenjaga(Anjing):
    def __init__(
        self,
        nama: str,
        usia: int,
        berat_badan: float,
        pemilik: Pemilik,
        warna: str,
        perawatan_khusus: list[dict[str, int | str]]
    ):
        super().__init__(nama, usia, berat_badan, pemilik)
        self.warna = warna
        self.perawatan_khusus = perawatan_khusus

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Usia: {self.usia}")
        print(f"Berat Badan: {self.berat_badan}")
        print(f"Pemilik: {self.pemilik.nama}")
        print(f"Warna: {self.warna}")
        for perawatan in self.perawatan_khusus:
            harga = f"{perawatan['harga']:,.0f}".replace(",", ".")
            print(f"---> Perawatan Khusus: {perawatan['nama']}\n---> Frekuensi: {perawatan['frekuensi']}x per hari\n---> Harga: Rp{harga}")
        print()