from __future__ import annotations

from Hewan.Kucing.kucing import Kucing
from Pemilik.pemilik import Pemilik

class KucingAnggora(Kucing):
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
