_dataPemilik = {}

class Pemilik:
    _counter = 1 

    def __init__(self, **kwargs):
        self.id_pemilik = f"PM{Pemilik._counter:03d}"  
        Pemilik._counter += 1

        self.nama = kwargs.get("nama")
        self.nomor_telepon = kwargs.get("nomor_telepon")  
        self.hewan_dimiliki = []

        _dataPemilik[self.id_pemilik] = {
            "nama": self.nama,
            "nomor_telepon": self.nomor_telepon
        }
    
    def addHewan(self, hewan):
        self.hewan_dimiliki.append(hewan)
        print(f"{hewan.nama} telah ditambahkan ke daftar hewan milik {self.nama}")
    
    def __str__(self):
        return (
            f'ID Pemilik: {self.id_pemilik}'
            f'Nama: {self.nama}'
            f'Nomor Telepon: {self.nomor_telepon}'
            f'Hewan Dimiliki: {", ".join([hewan.nama for hewan in self.hewan_dimiliki])}'
        )