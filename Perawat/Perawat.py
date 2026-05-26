_dataPerawat = {}

class Perawat:
    _counter = 1

    def __init__(self, **kwargs):
        self.id_perawat = f"P{Perawat._counter:03d}"
        Perawat._counter += 1

        self.nama = kwargs.get("nama")
        self.nomor_pegawai = kwargs.get("nomor_pegawai")

        print(f"Perawat {self.nama}({self.nomor_pegawai}) telah dibuat! Unique ID: {self.id_perawat}")
        _dataPerawat[self.id_perawat] = {
            "nama": self.nama,
            "nomor_pegawai": self.nomor_pegawai
        }
    
    def __str__(self):
        return f"Perawat(ID: {self.id_perawat}, Nama: {self.nama}, No Pegawai: {self.nomor_pegawai})"
    
class PerawatInap(Perawat):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tarif = kwargs.get("tarif", 50000)
        self.mulai_bertugas = kwargs.get("mulai_bertugas")
        self.hewan_ditangani = []
    
    def assignPet(self, hewan):
        self.hewan_ditangani.append(hewan)
        print(f"{hewan.nama} telah ditangani oleh {self.nama}")

    def __str__(self):
        return super().__str__() + f", Tarif: {self.tarif}, Mulai Bertugas: {self.mulai_bertugas}, Hewan Ditangani: {[hewan.nama for hewan in self.hewan_ditangani]}"