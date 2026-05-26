_dataDokter = {}


class Dokter:
    _counter = 1 

    def __init__(self, **kwargs):
        self.id_dokter = f"D{Dokter._counter:03d}" 
        Dokter._counter += 1

        self.nama = kwargs.get("nama")
        self.nomor_pegawai = kwargs.get("nomor_pegawai")

        print(f"Dokter {self.nama}({self.nomor_pegawai}) telah dibuat! Unique ID: {self.id_dokter}")
        _dataDokter[self.id_dokter] = {
            "nama": self.nama,
            "nomor_pegawai": self.nomor_pegawai
        }

    def __str__(self):
        return f"Dokter(ID: {self.id_dokter}, Nama: {self.nama}, No Pegawai: {self.nomor_pegawai})"
    
class DokterUmum(Dokter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tarif = kwargs.get("tarif", 100000)
        self.hewan_ditangani = []
        _dataDokter[self.id_dokter]["tarif"] = self.tarif        
        _dataDokter[self.id_dokter]["tipe"] = "Umum"             

    def assignPet(self, hewan):
        self.hewan_ditangani.append(hewan)
        print(f"{hewan.nama} telah ditangani oleh {self.nama}")
    
    def __str__(self):
        return super().__str__() + f", Tarif: {self.tarif}, Hewan Ditangani: {[hewan.nama for hewan in self.hewan_ditangani]}"
    
class DokterSpesialis(Dokter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spesialisasi = kwargs.get("spesialisasi")
        self.tarif = kwargs.get("tarif", 200000)
        self.hewan_ditangani = []
        _dataDokter[self.id_dokter]["spesialisasi"] = self.spesialisasi  
        _dataDokter[self.id_dokter]["tarif"] = self.tarif                
        _dataDokter[self.id_dokter]["tipe"] = "Spesialis"               

    def assignPet(self, hewan):
        self.hewan_ditangani.append(hewan)
        print(f"{hewan.nama} telah ditangani oleh {self.nama} (Spesialis {self.spesialisasi})")

    def __str__(self):
        return super().__str__() + f", Spesialisasi: {self.spesialisasi}, Tarif: {self.tarif}, Hewan Ditangani: {[hewan.nama for hewan in self.hewan_ditangani]}"