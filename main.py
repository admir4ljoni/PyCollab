from Tenaga_Layanan.tenaga_layanan import TenagaLayanan
from Tenaga_Layanan import tenaga_layanan
from Hewan.Anjing.anjing_kampung import AnjingKampung
from Hewan.Anjing.anjing_penjaga import AnjingPenjaga
from Hewan.Anjing import anjing_penjaga
from Hewan.Kucing.kucing_kampung import KucingKampung
from Hewan.Kucing import kucing_kampung
from Hewan.Kucing.kucing_anggora import KucingAnggora
from Tenaga_Layanan.Perawat.perawat_inap import PerawatInap
from Tenaga_Layanan.Perawat.perawat_grooming import PerawatGrooming
from Tenaga_Layanan.Dokter.dokter_spesialis import DokterSpesialis
from Tenaga_Layanan.Dokter.dokter_umum import DokterUmum
from Pemilik.pemilik import Pemilik
import Klinik.klinik as klinik

klinik_hewan_permata = klinik.Klinik(
    biaya_pemeriksaan_rutin = 200000,
    biaya_perawatan_khusus = 500000,
    biaya_perawatan_inap = 75000,
    biaya_perawatan_grooming = 250000
)

pemilik = Pemilik(
    nama = "Daniswara",
    narahubung = "1234-5678-9103"
)
pemilik_2 = Pemilik(
    nama = "arawsinaD",
    narahubung = "3019-8765-4321"
)

dokter_umum = DokterUmum(
    nama = "Tirta",
    nomor_pegawai = "K-1" 
)

dokter_spesialis = DokterSpesialis(
    nama = "Gia",
    nomor_pegawai = "K-2",
    biaya_khusus = 150000
)

perawat_grooming = PerawatGrooming(
    nama = "Yura",
    nomor_pegawai = "P-1"
)

perawat_inap = PerawatInap(
    nama = "Sasa",
    nomor_pegawai = "P-2",
    biaya_per_malam = 12000
)

kucing_anggora = KucingAnggora(
    nama = "Mochi",
    usia = 2,
    berat_badan = 2.3,
    pemilik = pemilik,
    warna = "Putih",
    perawatan_khusus = [
        {
            "nama": "pedicure",
            "harga": 50000
        }
    ]
)

kucing_kampung = KucingKampung(
    nama = "Oyen",
    usia = 1,
    berat_badan = 2.0,
    pemilik = pemilik_2,
    warna = "Coklat",
    perawatan_khusus=[]
)

anjing_penjaga = AnjingPenjaga(
    nama = "Kirik",
    usia = 2,
    berat_badan = 3.2,
    pemilik = pemilik,
    warna = "Coklat",
    perawatan_khusus = [
        {
            "nama": "pedicure",
            "harga": 50000
        },
        {
            "nama": "vaksinasi",
            "harga": 100000
        }
    ]
)

anjing_kampung = AnjingKampung(
    nama = "Kiko",
    usia = 1,
    berat_badan = 2.0,
    pemilik = pemilik_2,
    warna = "Coklat",
    perawatan_khusus=[]
) 


print("========== BIAYA KLINIK ==========")
print(f"Biaya Pemeriksaan Rutin: Rp{klinik_hewan_permata.biaya_pemeriksaan_rutin:,.0f}".replace(",", "."))
print(f"Biaya Perawatan Khusus: Rp{klinik_hewan_permata.biaya_perawatan_khusus:,.0f}".replace(",", "."))
print(f"Biaya Perawatan Inap: Rp{klinik_hewan_permata.biaya_perawatan_inap:,.0f}".replace(",", "."))
print(f"Biaya Perawatan Grooming: Rp{klinik_hewan_permata.biaya_perawatan_grooming:,.0f}".replace(",", "."))
print("==================================")

print("========== DATA HEWAN ==========")
print("Data Kucing Anggora: ")
kucing_anggora.tampilkan_data()
print("")
print("Data Kucing Kampung: ")
kucing_kampung.tampilkan_data()
print("")
print("Data Anjing Penjaga: ")
anjing_penjaga.tampilkan_data()
print("")
print("Data Anjing Kampung: ")
anjing_kampung.tampilkan_data()
print("==================================")

print("========== DATA LAYANAN ==========")
print("Data Pelayanan Kucing Anggora: ")
invoice = klinik_hewan_permata.hitung_biaya_perawatan(
    hewan = anjing_kampung,
    dokter = dokter_spesialis,
    perawat = perawat_inap,
    lama_rawat_inap = 10,
    jenis_perawatan = "khusus"
)
print(f"Nama Hewan: {invoice['hewan'].nama}")
print(f"Nama Pemilik: {invoice['hewan'].pemilik.nama}")
print(f"Jenis Hewan: {invoice['hewan'].__class__.__name__}")
print(f"Jenis Perawatan: {invoice['jenis_perawatan']}")
print(f"Nama Dokter: {invoice['nama_dokter']}")
print(f"Nama Perawat: {invoice['nama_perawat']}")
print(f"Lama Rawat Inap: {invoice['lama_rawat_inap']} hari")
print(f"Biaya Dasar: Rp{invoice['biaya_dasar']:,.0f}".replace(",", "."))
if invoice['biaya_spesialis'] > 0:
    print(f"Biaya Dokter Spesialis: Rp{invoice['biaya_spesialis']:,.0f}".replace(",", "."))
if invoice['biaya_rawat_inap'] > 0:
    print(f"Biaya Rawat Inap: Rp{invoice['biaya_rawat_inap']:,.0f}".replace(",", "."))
print("Perawatan Khusus:")
for perawatan in invoice['perawatan_khusus']:
    print(f"  - {perawatan['nama']}: Rp{perawatan['harga']:,.0f}".replace(",", "."))
print(f"Biaya Perawatan (Total): Rp{invoice['total']:,.0f}".replace(",", "."))

print()

TenagaLayanan.tampilkan_tenaga_layanan_berdasarkan_jenis(DokterUmum)
print()
pemilik.tampilkan_hewan_peliharaan_berdasarkan_jenis(jenis_hewan=KucingAnggora)