from __future__ import annotations

from Pemilik.pemilik import Pemilik

class Hewan:
    _registry: list[Hewan] = []

    def __init__(
        self,
        nama: str,
        usia: int,
        berat_badan: float, # berat badan di kg
        pemilik: Pemilik
    ):
        self.nama = nama
        self.usia = usia
        self.berat_badan = berat_badan
        self.pemilik = pemilik
        Hewan._registry.append(self)

    def tampilkan_data(
        self
        ):
        pass

    @classmethod
    def tampilkan_hewan_berdasarkan_jenis(
        cls,
        jenis_hewan: type
    ):
        pass