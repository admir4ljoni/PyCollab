from Dokter import Dokter

def main():
    while True:
        print("\n=== Menu Dokter ===")
        print("1. Tambah Dokter")
        print("2. Tampilkan Semua Dokter")
        print("3. Tambah Pasien ke Dokter")
        print("0. Keluar")

        opsi = int(input("Pilih menu: "))
        
        match opsi:
            case 1:
                temp_data = {}

                temp_data["id_dokter"] = str(input("ID Dokter: "))
                temp_data["nama_dokter"] = str(input("Nama Dokter: "))
                temp_data["spesialis_dokter"] = str(input("Spesialis Dokter: "))
                temp_data["narahubung_dokter"] = str(input("Narahubung Dokter: "))
                temp_data["tarif_dokter"] = int(input("Tarif Dokter: "))

                new_dokter = Dokter(**temp_data)
                print(f"Dokter '{new_dokter.nama_dokter}' berhasil ditambahkan.")
                continue
            case 2:
                semua_dokter = Dokter.getData()
                if semua_dokter:
                    for dokter in semua_dokter.values():
                        print(dokter)
                else:
                    print("Belum ada data dokter.")
                
                continue
            case 3:
                id_dokter = input("ID Dokter: ")
                id_hewan = input("ID Hewan (Pasien): ")
                try:
                    Dokter.assignPet(id_dokter, id_hewan)
                except ValueError as e:
                    print(e)

                continue
            case 0:
                print("Keluar dari program.")
                break
        


if __name__ == "__main__":
    main()