class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.tersedia = True

    def info(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} oleh {self.penulis} ({self.tahun}) - {status}"


class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if buku.tersedia:
            buku.tersedia = False
            self.buku_dipinjam.append(buku)
            print(f"{self.nama} berhasil meminjam '{buku.judul}'")
        else:
            print(f"Buku '{buku.judul}' sedang tidak tersedia")

    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            buku.tersedia = True
            self.buku_dipinjam.remove(buku)
            print(f"{self.nama} mengembalikan '{buku.judul}'")
        else:
            print(f"{self.nama} tidak meminjam buku ini")


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            print("-", buku.info())


# ====== SIMULASI ======
buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
buku2 = Buku("Bumi", "Tere Liye", 2014)

anggota1 = Anggota("Dito", "A001")

perpus = Perpustakaan()
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

perpus.tampilkan_buku()
print("="*30)

anggota1.pinjam_buku(buku1)
perpus.tampilkan_buku()
print("="*30)

anggota1.kembalikan_buku(buku1)
perpus.tampilkan_buku()