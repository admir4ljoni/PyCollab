class Ruang:
    _data = {}  

    def __init__(self, **kwargs):
        self.id_ruang       = kwargs.get("id_ruang")
        self.nama_ruang     = kwargs.get("nama_ruang")
        self.kapasitas_ruang = kwargs.get("kapasitas_ruang")
        Ruang._data[self.id_ruang] = self

    def getData(self, query=None):
        if query is None:
            return Ruang._data
        return Ruang._data.get(query)

    def __str__(self):
        return (f"Ruang       : {self.nama_ruang} "
                f"(ID: {self.id_ruang}, Kapasitas: {self.kapasitas_ruang})")