class Klinik:
    def __init__(self, **kwargs):
        self.nama_klinik = kwargs.get("nama klinik")
        self.alamat = kwargs.get("alamat")
        self.dokter = []
    
    def __str__(self):
        return (
            f'Nama Klinik: {self.nama_klinik}'
            f'Alamat: {self.alamat}'
            f'Dokter: {[dokter.nama for dokter in self.dokter]}'
        )
    
    def addDokter(self, dokter):
        self.dokter.append(dokter)
        print(f'{dokter.nama} ditambahkan ke {self.nama_klinik}')
