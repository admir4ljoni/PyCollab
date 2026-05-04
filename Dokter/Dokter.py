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