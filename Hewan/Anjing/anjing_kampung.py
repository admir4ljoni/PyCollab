from __future__ import annotations

from Hewan.Anjing.anjing import Anjing

class AnjingKampung(Anjing):
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