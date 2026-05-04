class Hewan:
    _data: dict[str, "Hewan"] = {}

    def __init__(self, id_hewan: str, nama_hewan: str, jenis_hewan: str, kondisi_hewan: str):
        self.id_hewan = id_hewan
        self.nama_hewan = nama_hewan
        self.jenis_hewan = jenis_hewan
        self.kondisi_hewan = kondisi_hewan
        self.riwayat_rawat_inap: list[dict] = []
        
        Hewan._data[self.id_hewan] = self
    
    @classmethod
    def create(cls, id_hewan: str, nama_hewan: str, jenis_hewan: str, kondisi_hewan: str) -> "Hewan":
        if id_hewan in cls._data:
            raise ValueError(f"Hewan dengan ID {id_hewan} sudah ada")
        
        return cls(id_hewan, nama_hewan, jenis_hewan, kondisi_hewan)

    @classmethod
    def get(cls, id_hewan: str) -> "Hewan | None":
        return cls._data.get(id_hewan)

    @classmethod
    def get_all(cls) -> list["Hewan"]:
        return list(cls._data.values())


    @classmethod
    def add_record(cls, id_hewan: str, id_dokter: str, id_ruang: str, id_pemilik: str, status_rawat_inap: bool, lama_rawat_inap: int) -> bool:
        from Dokter.dokter import Dokter
        from Ruang.ruang import Ruang
        from Pemilik.pemilik import Pemilik

        hewan = cls.get(id_hewan)

        if hewan is None:
            raise ValueError(f"Hewan dengan id {id_hewan} tidak ditemukan")

        if Dokter.get(id_dokter) is None:
            raise ValueError(f"Dokter dengan id {id_dokter} tidak ditemukan")
        
        if Ruang.get(id_ruang) is None:
            raise ValueError(f"Ruang dengan id {id_ruang} tidak ditemukan")

        if Pemilik.get(id_pemilik) is None:
            raise ValueError(f"Pemilik dengan id {id_pemilik} tidak ditemukan")

        riwayat = {
            "id_visit": len(hewan.riwayat_rawat_inap) + 1,
            "id_dokter": id_dokter,
            "id_ruang": id_ruang,
            "id_pemilik": id_pemilik,
            "status_rawat_inap": status_rawat_inap,
            "lama_rawat_inap": lama_rawat_inap
        }
        hewan.riwayat_rawat_inap.append(riwayat)

        return True
    
    @classmethod
    def update_record(cls, id_hewan: str, id_visit: int, **kwargs) -> "Hewan":
        hewan = cls.get(id_hewan)
        if hewan is None:
            raise ValueError(f"Hewan dengan id {id_hewan} tidak ditemukan")
        
        allowed_fields = {"id_dokter", "id_ruang", "id_pemilik", "status_rawat_inap", "lama_rawat_inap"}
        
        visit_record = None
        for record in hewan.riwayat_rawat_inap:
            if record.get("id_visit") == id_visit:
                visit_record = record
                break
        
        if visit_record is None:
            raise ValueError(f"Visit record dengan id {id_visit} tidak ditemukan")
        
        for key, value in kwargs.items():
            if key not in allowed_fields:
                raise ValueError(f"Field '{key}' tidak diperbolehkan")
            visit_record[key] = value
        
        return hewan

    def calculate_cost(self, id_visit: int) -> int:
        from Dokter.dokter import Dokter
        
        TARIF_INAP_PER_HARI = 200000
        
        visit_record = None
        for record in self.riwayat_rawat_inap:
            if record.get("id_visit") == id_visit:
                visit_record = record
                break
        
        if visit_record is None:
            raise ValueError(f"Visit record dengan id {id_visit} tidak ditemukan")
        
        dokter = Dokter.get(visit_record["id_dokter"])
        if dokter is None:
            raise ValueError(f"Dokter dengan id {visit_record['id_dokter']} tidak ditemukan")
        
        if visit_record["status_rawat_inap"]:
            return dokter.tarif_dokter + (TARIF_INAP_PER_HARI * visit_record["lama_rawat_inap"])
        return dokter.tarif_dokter

    @classmethod
    def get_by_dokter(cls, id_dokter: str) -> list["Hewan"]:
        from Dokter.dokter import Dokter

        if Dokter.get(id_dokter) is None:
            raise ValueError(f"Dokter dengan id {id_dokter} tidak ditemukan")

        assigned_pets = []
        
        for hewan in cls.get_all():
            for record in hewan.riwayat_rawat_inap:
                if record.get("id_dokter") == id_dokter:
                    assigned_pets.append(hewan)
                    break
        
        return assigned_pets

    @classmethod
    def get_by_pemilik(cls, id_pemilik: str) -> list["Hewan"]:
        from Pemilik.pemilik import Pemilik

        if Pemilik.get(id_pemilik) is None:
            raise ValueError(f"Pemilik dengan id {id_pemilik} tidak ditemukan")

        owned_pets = []
        
        for hewan in cls.get_all():
            for record in hewan.riwayat_rawat_inap:
                if record.get("id_pemilik") == id_pemilik:
                    owned_pets.append(hewan)
                    break
        
        return owned_pets

    @classmethod
    def delete(cls, id_hewan: str) -> bool:
        if id_hewan not in cls._data:
            return False
        
        del cls._data[id_hewan]
        return True

    def __str__(self) -> str:
        return (f"Hewan       : {self.nama_hewan}\n"
                f"ID: {self.id_hewan}\n"
                f"Jenis: {self.jenis_hewan}\n"
                f"Kondisi: {self.kondisi_hewan}")