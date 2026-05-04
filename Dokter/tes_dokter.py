import unittest
from io import StringIO
import sys

class Dokter:
    _data = {}
    
    def __init__(self, **kwargs):
        self.id_dokter = kwargs.get("id_dokter")
        self.nama_dokter = kwargs.get("nama_dokter")
        self.spesialis_dokter = kwargs.get("spesialis_dokter")
        self.narahubung_dokter = kwargs.get("narahubung_dokter")
        self.tarif_dokter = kwargs.get("tarif_dokter", 0)
        self.daftar_pasien = [] 
        
        Dokter._data[self.id_dokter] = self

    def getData(self, query=None):
        if query is None:
            return Dokter._data
        return Dokter._data.get(query)

    def assignPet(self, id_dokter, input=None):
        target_dokter = Dokter._data.get(id_dokter) if id_dokter else None
        if not target_dokter:
            raise ValueError("ID dokter tidak ditemukan.")
        if target_dokter and input:
            target_dokter.daftar_pasien.append(input)
            print(f"[assignPet] Hewan '{input}' ditambahkan ke "
                  f"dr. {target_dokter.nama_dokter}.")

    def __str__(self):
        return (f"Dokter      : {self.nama_dokter} "
                f"(Spesialis: {self.spesialis_dokter}, "
                f"Tarif: Rp {self.tarif_dokter:,})")

class TestDokter(unittest.TestCase):
    def setUp(self):
        Dokter._data = {}

    def test_01_init_dan_get_data_normal(self):
        dok = Dokter(id_dokter="D01", nama_dokter="Budi", spesialis_dokter="Kucing", tarif_dokter=50000)
        self.assertIn("D01", Dokter._data)
        self.assertEqual(dok.getData("D01").nama_dokter, "Budi")

    def test_02_assign_pet_normal(self):
        dok = Dokter(id_dokter="D01", nama_dokter="Budi", spesialis_dokter="Kucing")
        dok.assignPet("D01", "Kucing Hitam")
        self.assertIn("Kucing Hitam", dok.daftar_pasien)

    def test_03_assign_pet_invalid_id(self):
        dok = Dokter(id_dokter="D01", nama_dokter="Budi")
        with self.assertRaises(ValueError) as context:
            dok.assignPet("D99", "Anjing Puddle")
        self.assertEqual(str(context.exception), "ID dokter tidak ditemukan.")

    def test_04_vulnerability_str_tarif_string(self):
        dok = Dokter(id_dokter="D02", nama_dokter="Siti", tarif_dokter="Lima Puluh Ribu")
        with self.assertRaises(ValueError):
            print(dok)

    def test_05_vulnerability_duplicate_id_overwrite(self):
        Dokter(id_dokter="D01", nama_dokter="Budi")
        Dokter(id_dokter="D01", nama_dokter="Ahmad") # Menimpa Budi
        self.assertEqual(Dokter._data["D01"].nama_dokter, "Ahmad") # Budi hilang
        
    def test_06_vulnerability_none_id(self):
        dok = Dokter(nama_dokter="Tanpa ID")
        self.assertIn(None, Dokter._data)

if __name__ == "__main__":
    unittest.main()