from __future__ import annotations
from ..tenaga_layanan import TenagaLayanan

class Perawat(TenagaLayanan):
    def __init__(self, nama: str, nomor_pegawai: str):
        super().__init__(nama, nomor_pegawai)