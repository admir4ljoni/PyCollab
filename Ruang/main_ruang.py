from Ruang import Ruang

def main():
    # bikin object ruang
    r1 = Ruang(
        id_ruang="R1",
        nama_ruang="Ruang Operasi",
        kapasitas_ruang=5
    )

    r2 = Ruang(
        id_ruang="R2",
        nama_ruang="Ruang Rawat",
        kapasitas_ruang=10
    )

    # test print
    print(r1)
    print(r2)

    # test ambil data
    print("\nAmbil semua data:")
    print(Ruang._data)

    print("\nAmbil 1 data:")
    print(r1.getData("R1"))

if __name__ == "__main__":
    main()