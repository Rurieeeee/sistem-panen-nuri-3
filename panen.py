def hitung_total_panen(jumlah, harga):
    return jumlah * harga

jumlah = 100
harga = 5000

total = hitung_total_panen(jumlah, harga)

print("Jumlah panen:", jumlah, "kg")
print("Harga per kg: Rp", harga)
print("Total hasil panen: Rp", total)
