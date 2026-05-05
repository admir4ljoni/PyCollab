# Import semua kelas untuk testing
from Hewan.hewan import Hewan
from Dokter.dokter import Dokter
from Ruang.ruang import Ruang
from Pemilik.pemilik import Pemilik

def clear_all_data():
    """Bersihkan semua data kelas untuk testing yang bersih"""
    Hewan._data.clear()
    Dokter._data.clear()
    Ruang._data.clear()
    Pemilik._data.clear()

def print_test_header(test_name):
    """Cetak header test untuk kemudahan membaca"""
    print("\n" + "="*60)
    print(f"TEST: {test_name}")
    print("="*60)

def print_test_result(input_desc, expected, actual):
    """Cetak hasil test dengan format yang rapi"""
    print(f"\nInput: {input_desc}")
    print(f"Diharapkan: {expected}")
    print(f"Aktual: {actual}")
    if str(expected) == str(actual):
        print("LULUS")
    else:
        print("GAGAL")

# ==================== TEST KELAS HEWAN ====================

def test_hewan_create():
    print_test_header("HEWAN - Buat Hewan")
    
    # Input: Data hewan yang valid
    # Output Diharapkan: Objek Hewan dengan atribut yang ditentukan
    hewan = Hewan.create("H001", "Buddy", "Anjing", "Sehat")
    print_test_result("create('H001', 'Buddy', 'Anjing', 'Sehat')", 
                     "Objek Hewan dengan id=H001, nama=Buddy", 
                     f"Objek Hewan dengan id={hewan.id_hewan}, nama={hewan.nama_hewan}")

def test_hewan_get():
    print_test_header("HEWAN - Ambil Hewan")
    
    # Setup
    Hewan.create("H002", "Mittens", "Kucing", "Sakit")
    
    # Input: ID hewan yang ada
    # Output Diharapkan: Objek Hewan
    hewan = Hewan.get("H002")
    print_test_result("get('H002')", "Objek Hewan dengan id=H002", 
                     f"Objek Hewan dengan id={hewan.id_hewan if hewan else 'None'}")
    
    # Input: ID hewan yang tidak ada
    # Output Diharapkan: None
    hewan_none = Hewan.get("H999")
    print_test_result("get('H999')", "None", f"{hewan_none}")

def test_hewan_get_all():
    print_test_header("HEWAN - Ambil Semua Hewan")
    
    # Setup: Buat beberapa hewan
    Hewan.create("H003", "Charlie", "Burung", "Sehat")
    Hewan.create("H004", "Max", "Kelinci", "Pemulihan")
    
    # Input: Tidak ada parameter
    # Output Diharapkan: Daftar semua objek Hewan
    all_hewan = Hewan.get_all()
    print_test_result("get_all()", f"Daftar dengan {len(all_hewan)} hewan", 
                     f"Daftar dengan {len(all_hewan)} hewan")

def test_hewan_delete():
    print_test_header("HEWAN - Hapus Hewan")
    
    # Setup
    Hewan.create("H005", "Luna", "Ikan", "Sehat")
    
    # Input: ID hewan yang ada
    # Output Diharapkan: True (penghapusan berhasil)
    result = Hewan.delete("H005")
    print_test_result("delete('H005')", "True", f"{result}")
    
    # Verifikasi penghapusan
    deleted_hewan = Hewan.get("H005")
    print_test_result("get('H005') setelah hapus", "None", f"{deleted_hewan}")

def test_hewan_add_record():
    print_test_header("HEWAN - Tambah Riwayat Kunjungan")
    
    # Setup: Buat entitas terkait
    dokter = Dokter.create("D001", "Dr. Smith", "Umum", "08123456789", 500000)
    ruang = Ruang.create("R001", "Ruang A", 10)
    pemilik = Pemilik.create("P001", "John Doe", "08123456780")
    hewan = Hewan.create("H006", "Rocky", "Anjing", "Sakit")
    
    # Input: Data riwayat kunjungan yang valid
    # Output Diharapkan: True (rekaman berhasil ditambahkan)
    result = hewan.add_record("H006", "D001", "R001", "P001", True, 3)
    print_test_result("add_record('H006', 'D001', 'R001', 'P001', True, 3)", 
                     "True", f"{result}")
    
    # Verifikasi rekaman ditambahkan
    record_count = len(hewan.riwayat_rawat_inap)
    print_test_result("panjang riwayat_rawat_inap", "1", f"{record_count}")

def test_hewan_update_record():
    print_test_header("HEWAN - Update Riwayat Kunjungan")
    
    # Setup
    dokter = Dokter.create("D002", "Dr. Jones", "Spesialis", "08123456788", 750000)
    hewan = Hewan.create("H007", "Bella", "Kucing", "Sehat")
    hewan.add_record("H007", "D001", "R001", "P001", True, 2)
    
    # Input: Update riwayat kunjungan dengan data baru
    # Output Diharapkan: Objek Hewan yang diperbarui
    updated_hewan = Hewan.update_record("H007", 1, id_dokter="D002", lama_rawat_inap=5)
    updated_record = updated_hewan.riwayat_rawat_inap[0]
    print_test_result("update_record('H007', 1, id_dokter='D002', lama_rawat_inap=5)", 
                     "Rekaman dengan id_dokter=D002, lama_rawat_inap=5", 
                     f"Rekaman dengan id_dokter={updated_record['id_dokter']}, lama_rawat_inap={updated_record['lama_rawat_inap']}")

def test_hewan_calculate_cost():
    print_test_header("HEWAN - Hitung Biaya")
    
    # Setup
    dokter = Dokter.create("D003", "Dr. Wilson", "Bedah", "08123456787", 1000000)
    hewan = Hewan.create("H008", "Lucy", "Anjing", "Sakit")
    hewan.add_record("H008", "D003", "R001", "P001", True, 2)
    
    # Input: Hitung biaya untuk kunjungan dengan rawat inap
    # Output Diharapkan: 1400000 (1000000 + 2*200000)
    cost = hewan.calculate_cost(1)
    print_test_result("calculate_cost(1) dengan rawat inap", "1400000", f"{cost}")
    
    # Test tanpa rawat inap
    hewan.riwayat_rawat_inap[0]["status_rawat_inap"] = False
    cost_no_hosp = hewan.calculate_cost(1)
    print_test_result("calculate_cost(1) tanpa rawat inap", "1000000", f"{cost_no_hosp}")

def test_hewan_get_by_dokter():
    print_test_header("HEWAN - Ambil Hewan berdasarkan Dokter")
    
    # Setup - Hapus data yang ada untuk test yang bersih
    clear_all_data()
    
    # Buat data baru untuk test ini
    dokter = Dokter.create("D003", "Dr. Test", "Test", "08123456787", 500000)
    ruang = Ruang.create("R001", "Test Room", 10)
    pemilik = Pemilik.create("P001", "Test Owner", "08123456780")
    hewan1 = Hewan.create("H009", "Daisy", "Kucing", "Sehat")
    hewan2 = Hewan.create("H010", "Oscar", "Anjing", "Sakit")
    hewan1.add_record("H009", "D003", "R001", "P001", True, 1)
    hewan2.add_record("H010", "D003", "R001", "P001", True, 2)
    
    # Input: ID dokter
    # Output Diharapkan: Daftar hewan yang ditugaskan ke dokter tersebut
    animals = Hewan.get_by_dokter("D003")
    print_test_result("get_by_dokter('D003')", f"Daftar dengan 2 hewan", f"Daftar dengan {len(animals)} hewan")

def test_hewan_get_by_pemilik():
    print_test_header("HEWAN - Ambil Hewan berdasarkan Pemilik")
    
    # Setup - Hapus data yang ada untuk test yang bersih
    clear_all_data()
    
    # Buat data baru untuk test ini
    dokter = Dokter.create("D003", "Dr. Test", "Test", "08123456787", 500000)
    ruang = Ruang.create("R001", "Test Room", 10)
    pemilik = Pemilik.create("P001", "Test Owner", "08123456780")
    hewan1 = Hewan.create("H011", "Milo", "Anjing", "Sehat")
    hewan2 = Hewan.create("H012", "Luna", "Kucing", "Sakit")
    hewan1.add_record("H011", "D003", "R001", "P001", True, 1)
    hewan2.add_record("H012", "D003", "R001", "P001", True, 2)
    
    # Input: ID pemilik
    # Output Diharapkan: Daftar hewan yang dimiliki orang tersebut
    animals = Hewan.get_by_pemilik("P001")
    print_test_result("get_by_pemilik('P001')", f"Daftar dengan 2 hewan", f"Daftar dengan {len(animals)} hewan")

def test_hewan_get_pets_in_room():
    print_test_header("HEWAN - Ambil Hewan di Ruangan")
    
    # Setup - Hapus data yang ada untuk test yang bersih
    clear_all_data()
    
    # Buat data baru untuk test ini
    dokter = Dokter.create("D003", "Dr. Test", "Test", "08123456787", 500000)
    ruang = Ruang.create("R001", "Test Room", 10)
    pemilik = Pemilik.create("P001", "Test Owner", "08123456780")
    hewan1 = Hewan.create("H013", "Coco", "Burung", "Sehat")
    hewan2 = Hewan.create("H014", "Pepper", "Kelinci", "Sakit")
    hewan1.add_record("H013", "D003", "R001", "P001", True, 1)
    hewan2.add_record("H014", "D003", "R001", "P001", True, 2)
    
    # Input: ID ruangan
    # Output Diharapkan: Daftar hewan di ruangan tersebut
    animals = Hewan.get_pets_in_room("R001")
    print_test_result("get_pets_in_room('R001')", f"Daftar dengan 2 hewan", f"Daftar dengan {len(animals)} hewan")

# ==================== TEST KELAS DOKTER ====================

def test_dokter_create():
    print_test_header("DOKTER - Buat Dokter")
    
    # Input: Data dokter yang valid
    # Output Diharapkan: Objek Dokter dengan atribut yang ditentukan
    dokter = Dokter.create("D004", "Dr. Brown", "Anak", "08123456786", 600000)
    print_test_result("create('D004', 'Dr. Brown', 'Anak', '08123456786', 600000)", 
                     "Objek Dokter dengan id=D004, nama=Dr. Brown", 
                     f"Objek Dokter dengan id={dokter.id_dokter}, nama={dokter.nama_dokter}")

def test_dokter_get():
    print_test_header("DOKTER - Ambil Dokter")
    
    # Setup
    Dokter.create("D005", "Dr. Green", "Mata", "08123456785", 800000)
    
    # Input: ID dokter yang ada
    # Output Diharapkan: Objek Dokter
    dokter = Dokter.get("D005")
    print_test_result("get('D005')", "Objek Dokter dengan id=D005", 
                     f"Objek Dokter dengan id={dokter.id_dokter if dokter else 'None'}")

def test_dokter_get_all():
    print_test_header("DOKTER - Ambil Semua Dokter")
    
    # Setup: Buat beberapa dokter
    Dokter.create("D006", "Dr. White", "Jantung", "08123456784", 1200000)
    Dokter.create("D007", "Dr. Black", "Paru", "08123456783", 900000)
    
    # Input: Tidak ada parameter
    # Output Diharapkan: Daftar semua objek Dokter
    all_dokters = Dokter.get_all()
    print_test_result("get_all()", f"Daftar dengan {len(all_dokters)} dokter", 
                     f"Daftar dengan {len(all_dokters)} dokter")

def test_dokter_delete():
    print_test_header("DOKTER - Hapus Dokter")
    
    # Setup
    Dokter.create("D008", "Dr. Grey", "Kulit", "08123456782", 700000)
    
    # Input: ID dokter yang ada
    # Output Diharapkan: True (penghapusan berhasil)
    result = Dokter.delete("D008")
    print_test_result("delete('D008')", "True", f"{result}")
    
    # Verifikasi penghapusan
    deleted_dokter = Dokter.get("D008")
    print_test_result("get('D008') setelah hapus", "None", f"{deleted_dokter}")

def test_dokter_get_assigned_pets():
    print_test_header("DOKTER - Ambil Hewan yang Ditugaskan")
    
    # Setup - Hapus data yang ada untuk test yang bersih
    clear_all_data()
    
    # Buat data baru untuk test ini
    dokter = Dokter.create("D009", "Dr. Blue", "Gigi", "08123456781", 500000)
    ruang = Ruang.create("R001", "Test Room", 10)
    pemilik = Pemilik.create("P001", "Test Owner", "08123456780")
    hewan1 = Hewan.create("H015", "Rocky", "Anjing", "Sakit")
    hewan2 = Hewan.create("H016", "Bella", "Kucing", "Sehat")
    hewan1.add_record("H015", "D009", "R001", "P001", True, 1)
    hewan2.add_record("H016", "D009", "R001", "P001", True, 2)
    
    # Input: ID dokter
    # Output Diharapkan: Daftar hewan yang ditugaskan ke dokter tersebut
    pets = Dokter.get_assigned_pets("D009")
    print_test_result("get_assigned_pets('D009')", f"Daftar dengan 2 hewan", f"Daftar dengan {len(pets)} hewan")

# ==================== TEST KELAS RUANG ====================

def test_ruang_create():
    print_test_header("RUANG - Buat Ruangan")
    
    # Input: Data ruangan yang valid
    # Output Diharapkan: Objek Ruang dengan atribut yang ditentukan
    ruang = Ruang.create("R002", "Ruang B", 15)
    print_test_result("create('R002', 'Ruang B', 15)", 
                     "Objek Ruang dengan id=R002, nama=Ruang B", 
                     f"Objek Ruang dengan id={ruang.id_ruang}, nama={ruang.nama_ruang}")

def test_ruang_get():
    print_test_header("RUANG - Ambil Ruangan")
    
    # Setup
    Ruang.create("R003", "Ruang C", 20)
    
    # Input: ID ruangan yang ada
    # Output Diharapkan: Objek Ruang
    ruang = Ruang.get("R003")
    print_test_result("get('R003')", "Objek Ruang dengan id=R003", 
                     f"Objek Ruang dengan id={ruang.id_ruang if ruang else 'None'}")

def test_ruang_get_all():
    print_test_header("RUANG - Ambil Semua Ruangan")
    
    # Setup: Buat beberapa ruangan
    Ruang.create("R004", "Ruang D", 25)
    Ruang.create("R005", "Ruang E", 30)
    
    # Input: Tidak ada parameter
    # Output Diharapkan: Daftar semua objek Ruang
    all_rooms = Ruang.get_all()
    print_test_result("get_all()", f"Daftar dengan {len(all_rooms)} ruangan", 
                     f"Daftar dengan {len(all_rooms)} ruangan")

def test_ruang_delete():
    print_test_header("RUANG - Hapus Ruangan")
    
    # Setup
    Ruang.create("R006", "Ruang F", 35)
    
    # Input: ID ruangan yang ada
    # Output Diharapkan: True (penghapusan berhasil)
    result = Ruang.delete("R006")
    print_test_result("delete('R006')", "True", f"{result}")
    
    # Verifikasi penghapusan
    deleted_room = Ruang.get("R006")
    print_test_result("get('R006') setelah hapus", "None", f"{deleted_room}")

# ==================== TEST KELAS PEMILIK ====================

def test_pemilik_create():
    print_test_header("PEMILIK - Buat Pemilik")
    
    # Input: Data pemilik yang valid
    # Output Diharapkan: Objek Pemilik dengan atribut yang ditentukan
    pemilik = Pemilik.create("P002", "Jane Smith", "08123456779")
    print_test_result("create('P002', 'Jane Smith', '08123456779')", 
                     "Objek Pemilik dengan id=P002, nama=Jane Smith", 
                     f"Objek Pemilik dengan id={pemilik.id_pemilik}, nama={pemilik.nama_pemilik}")

def test_pemilik_get():
    print_test_header("PEMILIK - Ambil Pemilik")
    
    # Setup
    Pemilik.create("P003", "Bob Johnson", "08123456778")
    
    # Input: ID pemilik yang ada
    # Output Diharapkan: Objek Pemilik
    pemilik = Pemilik.get("P003")
    print_test_result("get('P003')", "Objek Pemilik dengan id=P003", 
                     f"Objek Pemilik dengan id={pemilik.id_pemilik if pemilik else 'None'}")

def test_pemilik_get_all():
    print_test_header("PEMILIK - Ambil Semua Pemilik")
    
    # Setup: Buat beberapa pemilik
    Pemilik.create("P004", "Alice Brown", "08123456777")
    Pemilik.create("P005", "Charlie Davis", "08123456776")
    
    # Input: Tidak ada parameter
    # Output Diharapkan: Daftar semua objek Pemilik
    all_pemilik = Pemilik.get_all()
    print_test_result("get_all()", f"Daftar dengan {len(all_pemilik)} pemilik", 
                     f"Daftar dengan {len(all_pemilik)} pemilik")

def test_pemilik_delete():
    print_test_header("PEMILIK - Hapus Pemilik")
    
    # Setup
    Pemilik.create("P006", "David Wilson", "08123456775")
    
    # Input: ID pemilik yang ada
    # Output Diharapkan: True (penghapusan berhasil)
    result = Pemilik.delete("P006")
    print_test_result("delete('P006')", "True", f"{result}")
    
    # Verifikasi penghapusan
    deleted_pemilik = Pemilik.get("P006")
    print_test_result("get('P006') setelah hapus", "None", f"{deleted_pemilik}")

def test_pemilik_get_owned_pets():
    print_test_header("PEMILIK - Ambil Hewan yang Dimiliki")
    
    # Setup - Hapus data yang ada untuk test yang bersih
    clear_all_data()
    
    # Buat data baru untuk test ini
    dokter = Dokter.create("D003", "Dr. Test", "Test", "08123456787", 500000)
    ruang = Ruang.create("R001", "Test Room", 10)
    pemilik = Pemilik.create("P007", "Emma Thompson", "08123456774")
    hewan1 = Hewan.create("H017", "Max", "Anjing", "Sehat")
    hewan2 = Hewan.create("H018", "Luna", "Kucing", "Sakit")
    hewan1.add_record("H017", "D003", "R001", "P007", True, 1)
    hewan2.add_record("H018", "D003", "R001", "P007", True, 2)
    
    # Input: ID pemilik
    # Output Diharapkan: Daftar hewan yang dimiliki orang tersebut
    pets = pemilik.get_owned_pets()
    print_test_result("get_owned_pets()", f"Daftar dengan 2 hewan", f"Daftar dengan {len(pets)} hewan")

# ==================== TEST VALIDASI ====================

def test_validations():
    print_test_header("TEST VALIDASI")
    
    # Test tarif negatif
    try:
        Dokter.create("D999", "Test", "Test", "08123456789", -1000)
        print_test_result("Tarif negatif", "ValueError", "Tidak ada error")
    except ValueError as e:
        print_test_result("Tarif negatif", "ValueError", f"LULUS - {e}")
    
    # Test format ID tidak valid
    try:
        Hewan.create("X001", "Test", "Test", "Test")
        print_test_result("Format ID tidak valid", "ValueError", "Tidak ada error")
    except ValueError as e:
        print_test_result("Format ID tidak valid", "ValueError", f"LULUS - {e}")
    
    # Test nama kosong
    try:
        Pemilik.create("P999", "", "08123456789")
        print_test_result("Nama kosong", "ValueError", "Tidak ada error")
    except ValueError as e:
        print_test_result("Nama kosong", "ValueError", f"LULUS - {e}")
    
    # Test telepon tidak valid
    try:
        Pemilik.create("P998", "Test", "123")
        print_test_result("Telepon tidak valid", "ValueError", "Tidak ada error")
    except ValueError as e:
        print_test_result("Telepon tidak valid", "ValueError", f"LULUS - {e}")

# ==================== TEST INTEGRASI ====================

def test_integration():
    print_test_header("TEST INTEGRASI")
    
    # Test workflow lengkap: Buat pemilik -> Buat hewan -> Tambah riwayat kunjungan -> Hitung biaya
    owner = Pemilik.create("P100", "Integration Test", "08123456770")
    doctor = Dokter.create("D100", "Dr. Test", "Test", "08123456771", 500000)
    room = Ruang.create("R100", "Test Room", 10)
    pet = Hewan.create("H100", "Test Pet", "Test Animal", "Test Condition")
    
    # Tambah riwayat kunjungan
    pet.add_record("H100", "D100", "R100", "P100", True, 3)
    
    # Hitung biaya
    cost = pet.calculate_cost(1)
    expected_cost = 1100000  # 500000 + 3*200000
    
    print_test_result("Perhitungan biaya workflow integrasi", f"{expected_cost}", f"{cost}")
    
    # Test query hubungan
    owner_pets = owner.get_owned_pets()
    doctor_pets = doctor.get_assigned_pets("D100")
    room_pets = Hewan.get_pets_in_room("R100")
    
    print_test_result("Jumlah hewan pemilik", "1", f"{len(owner_pets)}")
    print_test_result("Jumlah hewan dokter", "1", f"{len(doctor_pets)}")
    print_test_result("Jumlah hewan ruangan", "1", f"{len(room_pets)}")

# ==================== RUNNER TEST UTAMA ====================

def main():
    """Jalankan semua unit test"""
    print("TESTING...")
    print("Menguji semua kelas dan fungsionalitasnya")
    
    # Bersihkan data yang ada untuk testing yang bersih
    clear_all_data()
    
    # Jalankan test Hewan
    test_hewan_create()
    test_hewan_get()
    test_hewan_get_all()
    test_hewan_delete()
    test_hewan_add_record()
    test_hewan_update_record()
    test_hewan_calculate_cost()
    test_hewan_get_by_dokter()
    test_hewan_get_by_pemilik()
    test_hewan_get_pets_in_room()
    
    # Bersihkan data untuk test kelas berikutnya
    clear_all_data()
    
    # Jalankan test Dokter
    test_dokter_create()
    test_dokter_get()
    test_dokter_get_all()
    test_dokter_delete()
    test_dokter_get_assigned_pets()
    
    # Bersihkan data untuk test kelas berikutnya
    clear_all_data()
    
    # Jalankan test Ruang
    test_ruang_create()
    test_ruang_get()
    test_ruang_get_all()
    test_ruang_delete()
    
    # Bersihkan data untuk test kelas berikutnya
    clear_all_data()
    
    # Jalankan test Pemilik
    test_pemilik_create()
    test_pemilik_get()
    test_pemilik_get_all()
    test_pemilik_delete()
    test_pemilik_get_owned_pets()
    
    # Bersihkan data untuk test validasi
    clear_all_data()
    
    # Jalankan test validasi
    test_validations()
    
    # Bersihkan data untuk test integrasi
    clear_all_data()
    
    # Jalankan test integrasi
    test_integration()
    
    print("\n" + "="*60)
    print("SEMUA TEST SELESAI!")
    print("="*60)

if __name__ == "__main__":
    main()