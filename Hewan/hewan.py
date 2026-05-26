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
    def tampilkan_hewan_berdasarkan_jenis_atau_pemilik(
        cls,
        jenis_hewan: type | None = None,
        pemilik: Pemilik | None = None
    ):
        from Hewan.Anjing.anjing_kampung import AnjingKampung
        from Hewan.Anjing.anjing_penjaga import AnjingPenjaga
        from Hewan.Kucing.kucing_kampung import KucingKampung
        from Hewan.Kucing.kucing_anggora import KucingAnggora
        
        if jenis_hewan is None and pemilik is None:
            raise ValueError("Harus menyediakan setidaknya satu parameter: jenis_hewan atau pemilik")
        if jenis_hewan is not None and jenis_hewan not in (AnjingKampung, AnjingPenjaga, KucingKampung, KucingAnggora):
            raise TypeError("Hewan harus salah satu dari: KucingAnggora, KucingKampung, AnjingPenjaga, AnjingKampung")
        if pemilik is not None and not isinstance(pemilik, Pemilik):
            raise TypeError("Pemilik harus berupa instance dari kelas Pemilik")

        header = ""
        if jenis_hewan:
            header += f"Semua hewan berjenis {jenis_hewan.__name__}"
        if jenis_hewan and pemilik:
            header += " dan "
        if pemilik:
            header += f"milik {pemilik.nama}"
        print(header + ":\n")

        for hewan in cls._registry:
            match = True
            if jenis_hewan is not None and not isinstance(hewan, jenis_hewan):
                match = False
            if pemilik is not None and hewan.pemilik != pemilik:
                match = False
            
            if match:
                hewan.tampilkan_data()
                
        