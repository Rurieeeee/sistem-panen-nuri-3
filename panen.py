
def hitung_total_panen(jumlah, harga):
    return jumlah * harga

def hitung_diskon(total, persen_diskon):
    return total - (total * persen_diskon / 100)

jumlah = 100
harga = 5000
diskon = 10

total = hitung_total_panen(jumlah, harga)
total_setelah_diskon = hitung_diskon(total, diskon)

print("Jumlah panen:", jumlah, "kg")
print("Harga per kg: Rp", harga)
print("Total hasil panen: Rp", total)
print("Diskon:", diskon, "%")
print("Total setelah diskon: Rp", total_setelah_diskon)
