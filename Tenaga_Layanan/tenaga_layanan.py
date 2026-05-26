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
        pass

    def tampilkan_tenaga_layanan_berdasarkan_jenis(
        self,
        jenis_tenaga_layanan: type
    ):
        pass

