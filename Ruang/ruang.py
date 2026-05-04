class Ruang:
    _data: dict[str, "Ruang"] = {}

    def __init__(self, id_ruang: str, nama_ruang: str, kapasitas_ruang: int):
        self.id_ruang = id_ruang
        self.nama_ruang = nama_ruang
        self.kapasitas_ruang = kapasitas_ruang
        
        Ruang._data[self.id_ruang] = self
    
    # factory methods
    @classmethod
    def create(cls, id_ruang: str, nama_ruang: str, kapasitas_ruang: int) -> "Ruang":
        if id_ruang in cls._data:
            raise ValueError(f"Ruang dengan ID {id_ruang} sudah ada.")
        return cls(id_ruang, nama_ruang, kapasitas_ruang)

    @classmethod
    def get(cls, id_ruang: str) -> "Ruang | None":
        return cls._data.get(id_ruang)

    @classmethod
    def get_all(cls) -> list["Ruang"]:
        return list(cls._data.values())

    @classmethod
    def delete(cls, id_ruang: str) -> bool:
        if id_ruang not in cls._data:
            return False
        del cls._data[id_ruang]

        return True
        
    # dunder methods
    def __str__(self) -> str:
        return(
            f"Ruang: {self.nama_ruang}\n"
            f"ID ruang: {self.id_ruang}\n"
            f"Kapasitas ruang: {self.kapasitas_ruang}"
        )
