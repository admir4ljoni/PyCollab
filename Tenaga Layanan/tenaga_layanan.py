class TenagaLayanan:
    _registry: list[TenagaLayanan] = []

    def __init__(
        self,
        nama: str,
        nomor_pegawai: str
    ):
        self.nama = nama
        self.nomor_pegawai = nomor_pegawai
        TenagaLayanan._registry.append(self)
