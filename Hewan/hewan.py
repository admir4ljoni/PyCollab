class Hewan:
    _data = {}


    def __init__(self, **kwargs):
        self.id_hewan        = kwargs.get("id_hewan")
        self.nama_hewan      = kwargs.get("nama_hewan")
        self.jenis_hewan     = kwargs.get("jenis_hewan")
        self.kondisi_hewan   = kwargs.get("kondisi_hewan")
        self.status_rawat_inap = kwargs.get("status_rawat_inap", False)
        self.lama_rawat_inap = kwargs.get("lama_rawat_inap", 0)  
        self.dokter_hewan    = kwargs.get("dokter_hewan")          
        self.ruangan         = kwargs.get("ruangan")              
        Hewan._data[self.id_hewan] = self


    def getData(self, query=None):
        """Indexing hewan."""
        if query is None:
            return Hewan._data
        return Hewan._data.get(query)


    def saveData(self, query=None, input=None):
        target = Hewan._data.get(query) if query else self
        if target and isinstance(input, dict):
            for key, value in input.items():
                setattr(target, key, value)
            print(f"[saveData] Data hewan '{target.id_hewan}' diperbarui.")


    def hitung_tarif(self):
        TARIF_INAP_PER_HARI = 200_000
        dokter_obj = Dokter._data.get(self.dokter_hewan)
        tarif_dokter = dokter_obj.tarif_dokter if dokter_obj else 0


        if self.status_rawat_inap:
            total = tarif_dokter + (TARIF_INAP_PER_HARI * self.lama_rawat_inap)
        else:
            total = tarif_dokter
        return total


    def __str__(self):
        return (f"Hewan       : {self.nama_hewan} "
                f"(ID: {self.id_hewan}, Jenis: {self.jenis_hewan}, "
                f"Kondisi: {self.kondisi_hewan})")