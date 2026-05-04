class Ruang:
    _data: dict[str, "Ruang"] = {}

    def __init__(self, id_ruang: str, nama_ruang: str, kapasitas_ruang: int):
        self.id_ruang = id_ruang
        self.nama_ruang = nama_ruang
        self.kapasitas_ruang = kapasitas_ruang
        Ruang._data[self.id_ruang] = self
    
    # class factory
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
    def update(cls, id_ruang: str, **kwargs) -> "Ruang":
        ruang = cls.get(id_ruang)

        if ruang is None:
            raise ValueError(f"Ruang dengan ID {id_ruang} tidak ditemukan")
        
        if not kwargs:
            raise ValueError("Tidak ada field yang diperbarui")
        
        allowed_fields = {"nama_ruang", "kapasitas_ruang"}
        for key, value in kwargs.items():
            if key not in allowed_fields:
                raise ValueError(f"Field {key} tidak diperbolehkan")
            setattr(ruang, key, value)
        
        return ruang

    @classmethod
    def delete(cls, id_ruang: str) -> bool:
        if id_ruang not in cls._data:
            return False
        del cls._data[id_ruang]
        
        return True
        
