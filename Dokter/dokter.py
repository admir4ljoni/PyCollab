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
        
        # Validasi tarif
        if tarif_dokter < 0:
            raise ValueError("Tarif dokter tidak boleh negatif")
        if tarif_dokter > 10000000:  # Max 10 juta
            raise ValueError("Tarif dokter terlalu tinggi (maksimal Rp 10.000.000)")
        
        # Validasi nama
        if not nama_dokter.strip():
            raise ValueError("Nama dokter tidak boleh kosong")
        if len(nama_dokter) > 100:
            raise ValueError("Nama dokter terlalu panjang (maksimal 100 karakter)")
        
        # Validasi spesialis
        if not spesialis_dokter.strip():
            raise ValueError("Spesialis dokter tidak boleh kosong")
        if len(spesialis_dokter) > 50:
            raise ValueError("Spesialis dokter terlalu panjang (maksimal 50 karakter)")
        
        # Validasi narahubung
        if not narahubung_dokter.strip():
            raise ValueError("Narahubung dokter tidak boleh kosong")
        if len(narahubung_dokter) < 10 or len(narahubung_dokter) > 15:
            raise ValueError("Nomor telepon tidak valid (10-15 digit)")
        if not narahubung_dokter.startswith('08'):
            raise ValueError("Nomor telepon harus dimulai dengan 08")
        
        # Validasi format ID
        if not id_dokter.startswith('D'):
            raise ValueError("ID dokter harus dimulai dengan 'D'")
        if len(id_dokter) != 4:
            raise ValueError("ID dokter harus 4 karakter (contoh: D001)")
        if not id_dokter[1:].isdigit():
            raise ValueError("ID dokter harus diikuti angka (contoh: D001)")

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