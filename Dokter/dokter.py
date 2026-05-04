class Dokter:
    _data: dict[str, "Dokter"] = {}

    def __init__(
        self,
        id_dokter: str,
        nama_dokter: str,
        spesialis_dokter: str,
        narahubung_dokter: str,
        tarif_dokter: int
    ):
        self.id_dokter = id_dokter
        self.nama_dokter = nama_dokter
        self.spesialis_dokter = spesialis_dokter
        self.narahubung_dokter = narahubung_dokter
        self.tarif_dokter = tarif_dokter
        
        Dokter._data[self.id_dokter] = self

    @classmethod
    def create(cls, id_dokter: str, nama_dokter: str, spesialis_dokter: str, narahubung_dokter: str, tarif_dokter: int) -> "Dokter":
        if id_dokter in cls._data:
            raise ValueError(f"Dokter dengan ID {id_dokter} sudah ada")

        return cls(id_dokter, nama_dokter, spesialis_dokter, narahubung_dokter, tarif_dokter)

    @classmethod
    def get(cls, id_dokter: str) -> "Dokter | None":
        return cls._data[id_dokter]

    @classmethod
    def get_all(cls) -> list["Dokter"]:
        return list(cls._data.values())

    @classmethod
    def get_assigned_pets(cls, id_dokter: str) -> list["Hewan"]:
        from Hewan.hewan import Hewan
        
        return Hewan.get_by_dokter(id_dokter)

    @classmethod
    def delete(cls, id_dokter: str) -> bool:
        if id_dokter not in cls._data:
            return False
        
        del cls._data[id_dokter]
        return True

    def __str__(self) -> str:
        return(
            f"Dokter: {self.nama_dokter}\n"
            f"ID dokter: {self.id_dokter}\n"
            f"Spesialis dokter: {self.spesialis_dokter}\n"
            f"Narahubung dokter: {self.narahubung_dokter}\n"
            f"Tarif dokter: {self.tarif_dokter}"
        )