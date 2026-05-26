import Klinik.klinik as klinik
import Hewan.hewan as hewan
import Pemilik.pemilik as pemilik
import Tenaga_Layanan.tenaga_layanan as tenaga_layanan

klinik = klinik.Klinik(100000, 500000, 1000000, 250000)
hewan = hewan.Hewan("hazon", 2, 5, pemilik)
pemilik = pemilik.Pemilik("John", "1234567890")
tenaga_layanan = tenaga_layanan.TenagaLayanan("John", "k-1")
