from Hewan.hewan import Hewan
from Pemilik.pemilik import Pemilik

class Kucing(Hewan):
    def __init__(
        self,
        nama: str,
        usia: int,
        berat_badan: float,
        pemilik: Pemilik
    ):
        super().__init__(nama, usia, berat_badan, pemilik)
        