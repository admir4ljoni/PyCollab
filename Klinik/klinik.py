from __future__ import annotations

from Tenaga_Layanan.Dokter.dokter import Dokter
from Tenaga_Layanan.Dokter.dokter_spesialis import DokterSpesialis
from Tenaga_Layanan.Perawat.perawat import Perawat
from Tenaga_Layanan.Perawat.perawat_inap import PerawatInap
from Tenaga_Layanan.Perawat.perawat_grooming import PerawatGrooming 
from Hewan.hewan import Hewan

class Klinik:
    def __init__(
        self,
        biaya_pemeriksaan_rutin: int,
        biaya_perawatan_khusus: int,
        biaya_perawatan_inap: int,
        biaya_perawatan_grooming: int
    ):

        if not isinstance(biaya_pemeriksaan_rutin, int):
            raise TypeError("Biaya pemeriksaan rutin harus berupa integer")
        if biaya_pemeriksaan_rutin < 0:
            raise ValueError("Biaya pemeriksaan rutin tidak boleh negatif")

        if not isinstance(biaya_perawatan_khusus, int):
            raise TypeError("Biaya perawatan khusus harus berupa integer")
        if biaya_perawatan_khusus < 0:
            raise ValueError("Biaya perawatan khusus tidak boleh negatif")

        if not isinstance(biaya_perawatan_inap, int):
            raise TypeError("Biaya perawatan inap harus berupa integer")
        if biaya_perawatan_inap < 0:
            raise ValueError("Biaya perawatan inap tidak boleh negatif")

        if not isinstance(biaya_perawatan_grooming, int):
            raise TypeError("Biaya perawatan grooming harus berupa integer")
        if biaya_perawatan_grooming < 0:
            raise ValueError("Biaya perawatan grooming tidak boleh negatif")

        self.biaya_pemeriksaan_rutin = biaya_pemeriksaan_rutin
        self.biaya_perawatan_khusus = biaya_perawatan_khusus
        self.biaya_perawatan_inap = biaya_perawatan_inap
        self.biaya_perawatan_grooming = biaya_perawatan_grooming

    def hitung_biaya_perawatan(
        self,
        dokter: Dokter | None = None,
        perawat: Perawat | None = None,
        hewan: Hewan | None = None,
        lama_rawat_inap: int = 0,
        jenis_perawatan: str = "pemeriksaan" # opsi perawatan HANYA = "khusus", "inap", "grooming", dan "pemeriksaan"
    ):
        if not isinstance(lama_rawat_inap, int):
            raise TypeError("Lama rawat inap harus berupa integer")
        if lama_rawat_inap < 0:
            raise ValueError("Lama rawat inap tidak boleh negatif")
        if jenis_perawatan.lower() not in ["khusus", "inap", "grooming", "pemeriksaan"]:
            raise ValueError("Jenis perawatan harus salah satu dari: khusus, inap, grooming, pemeriksaan")

        total = 0
        biaya_dasar = 0
        for perawatan_khusus in hewan.perawatan_khusus:
            total += perawatan_khusus["harga"]

        if jenis_perawatan.lower() == "pemeriksaan" and isinstance(dokter, Dokter):
            biaya_dasar = self.biaya_pemeriksaan_rutin
            total += self.biaya_pemeriksaan_rutin
        elif jenis_perawatan.lower() == "khusus" and isinstance(dokter, DokterSpesialis):
            biaya_dasar = self.biaya_perawatan_khusus
            total += dokter.biaya_khusus
            total += self.biaya_perawatan_khusus
        elif jenis_perawatan.lower() == "inap" and isinstance(perawat, PerawatInap):
            biaya_dasar = self.biaya_perawatan_inap
            total += (perawat.biaya_per_malam * lama_rawat_inap)
            total += self.biaya_perawatan_inap
        elif jenis_perawatan.lower() == "grooming" and isinstance(perawat, PerawatGrooming):
            biaya_dasar = self.biaya_perawatan_grooming
            total += self.biaya_perawatan_grooming
        else:
            raise ValueError("Jenis perawatan tidak sesuai dengan tenaga layanan yang diberikan")
        
        invoice = {
            "total": total,
            "biaya_dasar": biaya_dasar,
            "perawatan_khusus": [
                perawatan_khusus for perawatan_khusus in hewan.perawatan_khusus
            ],
            "jenis_perawatan": jenis_perawatan,
            "lama_rawat_inap": lama_rawat_inap if lama_rawat_inap else 0,
            "nama_dokter": dokter.nama if dokter else None,
            "nama_perawat": perawat.nama if perawat else None,
            "nama_hewan": hewan.nama if hewan else None
        }
        return invoice
        