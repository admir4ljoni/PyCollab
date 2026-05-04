class Pemilik:
    _data: dict[str, "Pemilik"] = {}

    def __init__(self, id_pemilik: str, nama_pemilik: str, narahubung_pemilik: str):
        self.id_pemilik         = id_pemilik
        self.nama_pemilik       = nama_pemilik
        self.narahubung_pemilik = narahubung_pemilik
        
        Pemilik._data[self.id_pemilik] = self

    @classmethod
    def create(cls, id_pemilik: str, nama_pemilik: str, narahubung_pemilik: str) -> "Pemilik":
        if id_pemilik in cls._data:
            raise ValueError(f"Pemilik dengan ID {id_pemilik} sudah ada.")
        
        # Validasi nama
        if not nama_pemilik.strip():
            raise ValueError("Nama pemilik tidak boleh kosong")
        if len(nama_pemilik) > 100:
            raise ValueError("Nama pemilik terlalu panjang (maksimal 100 karakter)")
        
        # Validasi narahubung
        if not narahubung_pemilik.strip():
            raise ValueError("Narahubung pemilik tidak boleh kosong")
        if len(narahubung_pemilik) < 10 or len(narahubung_pemilik) > 15:
            raise ValueError("Nomor telepon tidak valid (10-15 digit)")
        if not narahubung_pemilik.startswith('08'):
            raise ValueError("Nomor telepon harus dimulai dengan 08")
        
        # Validasi format ID
        if not id_pemilik.startswith('P'):
            raise ValueError("ID pemilik harus dimulai dengan 'P'")
        if len(id_pemilik) != 4:
            raise ValueError("ID pemilik harus 4 karakter (contoh: P001)")
        if not id_pemilik[1:].isdigit():
            raise ValueError("ID pemilik harus diikuti angka (contoh: P001)")
        
        return cls(id_pemilik, nama_pemilik, narahubung_pemilik)

    @classmethod
    def get(cls, id_pemilik: str) -> "Pemilik | None":
        return cls._data.get(id_pemilik)

    @classmethod
    def get_all(cls) -> list["Pemilik"]:
        return list(cls._data.values())

    @classmethod
    def delete(cls, id_pemilik: str) -> bool:
        if id_pemilik not in cls._data:
            return False
        del cls._data[id_pemilik]
        return True

    def get_owned_pets(self) -> list["Hewan"]:
        """Get all pets owned by this pemilik using Hewan.get_by_pemilik"""
        from Hewan.hewan import Hewan
        return Hewan.get_by_pemilik(self.id_pemilik)

    def tampilkan_info_lengkap(self) -> None:
        # Import di dalam method untuk menghindari circular import
        from Hewan.hewan import Hewan
        from Dokter.dokter import Dokter
        from Ruang.ruang import Ruang

        TARIF_INAP_PER_HARI = 200_000
        print("=" * 60)
        print(f"PEMILIK     : {self.nama_pemilik}")
        print(f"ID Pemilik  : {self.id_pemilik}")
        print(f"Narahubung  : {self.narahubung_pemilik}")
        print("-" * 60)

        owned_pets = self.get_owned_pets()
        
        for hewan in owned_pets:
            print(str(hewan))
            print(f"  Kondisi   : {hewan.kondisi_hewan}")

            # Get the latest visit record for this animal
            latest_record = None
            if hewan.riwayat_rawat_inap:
                latest_record = hewan.riwayat_rawat_inap[-1]  # Get most recent record

            if latest_record:
                dokter = Dokter.get(latest_record["id_dokter"])
                if dokter:
                    print(f"  {dokter}")
                    print(f"  Narahubung Dokter : {dokter.narahubung_dokter}")
                else:
                    print("  Dokter      : (tidak ada)")

                ruang = Ruang.get(latest_record["id_ruang"])
                if ruang:
                    print(f"  {ruang}")
                else:
                    print("  Ruang       : (tidak ada / tidak rawat inap)")

                status_str = (
                    f"Rawat Inap ({latest_record['lama_rawat_inap']} hari)"
                    if latest_record["status_rawat_inap"] else "Tanpa Rawat Inap"
                )
                
                # Calculate cost using the calculate_cost method
                try:
                    total = hewan.calculate_cost(latest_record["id_visit"])
                    tarif_dokter = dokter.tarif_dokter if dokter else 0
                except:
                    total = 0
                    tarif_dokter = 0

                print(f"  Status      : {status_str}")
                print(f"  Rincian Tarif:")
                print(f"    - Tarif Dokter      : Rp {tarif_dokter:>10,}")
                if latest_record["status_rawat_inap"]:
                    biaya_inap = TARIF_INAP_PER_HARI * latest_record["lama_rawat_inap"]
                    print(f"    - Biaya Rawat Inap  : Rp {biaya_inap:>10,} "
                          f"(Rp 200.000 × {latest_record['lama_rawat_inap']} hari)")
                print(f"    ──────────────────────────────")
                print(f"    TOTAL               : Rp {total:>10,}")
            else:
                print("  Dokter      : (tidak ada)")
                print("  Ruang       : (tidak ada / tidak rawat inap)")
                print("  Status      : Tidak ada riwayat perawatan")
            
            print("-" * 60)

        print("=" * 60)

    def __str__(self) -> str:
        return (f"Pemilik: {self.nama_pemilik} "
                f"(ID: {self.id_pemilik}, "
                f"HP: {self.narahubung_pemilik})")