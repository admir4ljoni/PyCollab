from __future__ import annotations

from Tenaga_Layanan.Dokter.dokter import Dokter
from Tenaga_Layanan.Perawat.perawat import Perawat
from Hewan.hewan import Hewan

class Klinik:
    def __init__(
        self,
        biaya_pemeriksaan_rutin: int,
        biaya_perawatan_khusus: int,
        biaya_perawatan_inap: int,
        biaya_perawatan_grooming: int
    ):
        self.biaya_pemeriksaan_rutin = biaya_pemeriksaan_rutin
        self.biaya_perawatan_khusus = biaya_perawatan_khusus
        self.biaya_perawatan_inap = biaya_perawatan_inap
        self.biaya_perawatan_grooming = biaya_perawatan_grooming

    def hitung_biaya_perawatan(
        self,
        dokter: Dokter | None,
        perawat: Perawat | None,
        hewan: Hewan | None,
        lama_rawat_inap: int = 0,
        jenis_perawatan: str = "pemeriksaan" # opsi perawatan HANYA = "khusus", "inap", "grooming", dan "pemeriksaan"
    ):
        pass