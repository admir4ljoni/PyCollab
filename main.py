from Klinik import Klinik
from Dokter import Dokter, DokterUmum, DokterSpesialis
from Hewan import Hewan, Kucing, Anjing
from Perawat import Perawat, PerawatInap
from Perawat import _dataPerawat as dataPerawat
from Dokter import _dataDokter as dataDokter
from Pemilik import Pemilik
from Hewan import _dataHewan as dataHewan

def database_dokter():
    while True:
        print("-"*15 + "[DATABASE DOKTER]" + "-"*15)
        print("1. Tambah Dokter")
        print("2. Tampilkan Semua Dokter")
        print("3. Cari Dokter")
        print("0. Kembali ke Menu Utama")

        pilihan = int(input("Pilih menu: "))

        match pilihan:
            case 1:
                print("1. Dokter Umum")
                print("2. Dokter Spesialis")
                jenis = int(input("Pilih jenis dokter: "))
                nomor_pegawai = input("Masukkan nomor pegawai: ")
                nama = input("Masukkan nama dokter: ")
                if jenis == 1:
                    tarif = int(input("Masukkan tarif dokter umum: "))
                    temp = DokterUmum(nama=nama, nomor_pegawai=nomor_pegawai, tarif=tarif)
                elif jenis == 2:
                    tarif = int(input("Masukkan tarif dokter spesialis: "))
                    spesialisasi = input("Masukkan spesialisasi: ")
                    temp = DokterSpesialis(nama=nama, nomor_pegawai=nomor_pegawai, spesialisasi=spesialisasi, tarif=tarif)
                else:
                    print("Jenis dokter tidak valid!")
                    continue
            case 2:
                print(dataDokter)
                continue
            # main.py — database_dokter() case 3
            case 3:
                id_cari = input("Masukkan ID Dokter yang ingin dicari: ").strip().upper()  # normalize input
                if id_cari in dataDokter:
                    info = dataDokter[id_cari]
                    print(f"Dokter ditemukan: ID: {id_cari}, Nama: {info['nama']}, No Pegawai: {info['nomor_pegawai']}")
                else:
                    print("Dokter tidak ditemukan!")
                continue
            case 0:
                break
            case _:
                print("Pilihan tidak valid!")

def database_hewan():
    while True:
        print("-"*15 + "[DATABASE HEWAN]" + "-"*15)
        print("1. Tambah Hewan")
        print("2. Tampilkan Semua Hewan")
        print("3. Cari Hewan")
        print("0. Kembali ke Menu Utama")

        pilihan = int(input("Pilih menu: "))

        match pilihan:
            case 1:
                print("1. Kucing\n2. Anjing")
                jenis = int(input("Pilih jenis hewan: "))
                nama = input("Nama: ")
                usia = int(input("Usia (tahun): "))
                berat = float(input("Berat (kg): "))
                id_pemilik = input("ID Pemilik: ")
                if jenis == 1:
                    jenis_bulu = input("Jenis Bulu: ")
                    temp = Kucing(nama=nama, usia=usia, berat=berat, id_pemilik=id_pemilik, jenis_bulu=jenis_bulu)
                elif jenis == 2:
                    jenis_ras = input("Jenis Ras: ")
                    temp = Anjing(nama=nama, usia=usia, berat=berat, id_pemilik=id_pemilik, jenis_ras=jenis_ras)
                print(temp)
            case 2:
                print(dataHewan)
            case 3:
                id_cari = input("Masukkan ID Hewan: ").strip().upper()
                if id_cari in dataHewan:
                    print(dataHewan[id_cari])
                else:
                    print("Hewan tidak ditemukan!")
            case 0:
                break
            case _:
                print("Pilihan tidak valid!")

def database_pemilik():
    pass

def database_perawat():
    while True:
        print("-"*15 + "[DATABASE PERAWAT]" + "-"*15)
        print("1. Tambah Perawat")
        print("2. Tampilkan Semua Perawat")
        print("3. Cari Perawat")
        print("0. Kembali ke Menu Utama")

        pilihan = int(input("Pilih menu: "))

        match pilihan:
            case 1:
                nama = input("Masukkan nama perawat: ")
                nomor_pegawai = input("Masukkan nomor pegawai: ")
                tarif = int(input("Masukkan tarif perawat inap (default 50000): ") or 50000)
                temp = PerawatInap(nama=nama, nomor_pegawai=nomor_pegawai, tarif=tarif)
                print(temp)
                continue
            case 2:
                print(dataPerawat)
                continue
            case 3:
                id_cari = input("Masukkan ID Perawat yang ingin dicari: ").strip().upper()
                for id_perawat, info in dataPerawat.items():
                    if id_perawat == id_cari:
                        print(f"Perawat ditemukan: ID: {id_perawat}, Nama: {info['nama']}, No Pegawai: {info['nomor_pegawai']}")
                        break
                else:
                    print("Perawat tidak ditemukan!")
                continue
            case 0:
                break
            case _:
                print("Pilihan tidak valid!")

def main():
    while True:
        print("-"*15 + "[SISTEM KLINIK PERAWATAN HEWAN]" + "-"*15)
        print("1. Database Dokter")
        print("2. Database Pemilik")
        print("3. Database Hewan")
        print("4. Database Perawat")
        print("0. Keluar")

        pilihan = int(input("Pilih menu: "))

        match pilihan:
            case 1:
                database_dokter()
                continue
            case 2:
                database_pemilik()
                continue
            case 3:
                database_hewan()
                continue
            case 4:
                database_perawat()
                continue
            case 0:
                print("Terima kasih!")
                exit()
            case _:
                print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()