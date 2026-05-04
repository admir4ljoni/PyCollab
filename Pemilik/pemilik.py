class Pemilik:
    _data = {}

    def __init__(self, **kwargs):
        """Menerima input dan menyimpan informasi tentang pemilik."""
        self.id_pemilik       = kwargs.get("id_pemilik")
        self.nama_pemilik     = kwargs.get("nama_pemilik")
        self.narahubung_pemilik = kwargs.get("narahubung_pemilik")
        self.daftar_hewan     = kwargs.get("daftar_hewan", [])     
        Pemilik._data[self.id_pemilik] = self

    def getData(self, query=None):
        """Indexing pemilik."""
        if query is None:
            return Pemilik._data
        return Pemilik._data.get(query)

    def tampilkan_info_lengkap(self):
        """
        Menampilkan informasi lengkap:
        pemilik → hewan peliharaan → dokter penanganan → ruang perawatan
        beserta total tarif periksa.
        """
        TARIF_INAP_PER_HARI = 200_000
        print("=" * 60)
        print(f"PEMILIK     : {self.nama_pemilik}")
        print(f"ID Pemilik  : {self.id_pemilik}")
        print(f"Narahubung  : {self.narahubung_pemilik}")
        print("-" * 60)

        for id_hw in self.daftar_hewan:
            hewan = Hewan._data.get(id_hw)
            if not hewan:
                continue

            print(str(hewan))
            print(f"  Kondisi   : {hewan.kondisi_hewan}")

            dokter = Dokter._data.get(hewan.dokter_hewan)
            if dokter:
                print(f"  {dokter}")
                print(f"  Narahubung Dokter : {dokter.narahubung_dokter}")
            else:
                print("  Dokter      : (tidak ada)")

            ruang = Ruang._data.get(hewan.ruangan)
            if ruang:
                print(f"  {ruang}")
            else:
                print("  Ruang       : (tidak ada / tidak rawat inap)")

            status_str = (
                f"Rawat Inap ({hewan.lama_rawat_inap} hari)"
                if hewan.status_rawat_inap else "Tanpa Rawat Inap"
            )
            total = hewan.hitung_tarif()
            tarif_dokter = dokter.tarif_dokter if dokter else 0

            print(f"  Status      : {status_str}")
            print(f"  Rincian Tarif:")
            print(f"    - Tarif Dokter      : Rp {tarif_dokter:>10,}")
            if hewan.status_rawat_inap:
                biaya_inap = TARIF_INAP_PER_HARI * hewan.lama_rawat_inap
                print(f"    - Biaya Rawat Inap  : Rp {biaya_inap:>10,} "
                      f"(Rp 200.000 × {hewan.lama_rawat_inap} hari)")
            print(f"    ──────────────────────────────")
            print(f"    TOTAL               : Rp {total:>10,}")
            print("-" * 60)

        print("=" * 60)

    def __str__(self):
        return (f"Pemilik: {self.nama_pemilik} "
                f"(ID: {self.id_pemilik}, "
                f"HP: {self.narahubung_pemilik})")
    
