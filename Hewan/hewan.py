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
        if not isinstance(usia, int):
            raise TypeError("Usia harus berupa integer")
        if usia < 0:
            raise ValueError("Usia tidak boleh negatif")
        
        if not isinstance(berat_badan, (float, int)):
            raise TypeError("Berat badan harus berupa float atau integer")
        if berat_badan < 0:
            raise ValueError("Berat badan tidak boleh negatif")
        
        if not isinstance(pemilik, Pemilik):
            raise TypeError("Pemilik harus berupa instance dari kelas Pemilik")

        self.nama = nama
        self.usia = usia
        self.berat_badan = berat_badan
        self.pemilik = pemilik
        Hewan._registry.append(self)

    def tampilkan_data(self):
        print(f"Salah memanggil objek {self.__class__.__name__}, silahkan gunakan method tampilkan_data() dari kelas turunan")

    @classmethod
    def tampilkan_hewan_berdasarkan_jenis(
        cls,
        jenis_hewan: type
    ):
        print(f"Semua hewan berjenis {jenis_hewan.__name__}:")
        for hewan in cls._registry:
            if isinstance(hewan, jenis_hewan):
                hewan.tampilkan_data()
                
        