from __future__ import annotations
from Tenaga_Layanan.tenaga_layanan import TenagaLayanan

class Dokter(TenagaLayanan):
    def __init__(self, nama: str, nomor_pegawai: str):
        super().__init__(nama, nomor_pegawai)