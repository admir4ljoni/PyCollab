from __future__ import annotations

class TenagaLayanan:
    _registry: list[TenagaLayanan] = []

    def __init__(
        self,
        nama: str,
        nomor_pegawai: str
    ):
        self.nama = nama
        self.nomor_pegawai = nomor_pegawai
        TenagaLayanan._registry.append(self)

    def tampilkan_data(self):
        print(f"Salah memanggil objek {self.__class__.__name__}, silahkan gunakan method tampilkan_data() dari kelas turunan")

    @classmethod
    def tampilkan_tenaga_layanan_berdasarkan_jenis(
        cls,
        jenis_tenaga_layanan: type
    ):
        for karyawan in cls._registry:
            if isinstance(karyawan, jenis_tenaga_layanan):
                karyawan.tampilkan_data()

