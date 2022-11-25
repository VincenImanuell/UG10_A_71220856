print("==== Selamat datang di Toko Andi Tersenyum, selamat belanja! ====")
total = int(input("Total belanja : Rp. "))

if total >= 1000000:
    biaya = total-(total*(10/100))
    print("Biaya yang harus dibayar setelah diskon adalah: ", biaya)
elif total < 1000000 and total >= 500000:
    biaya = total-(total*(5/100))
    print("Biaya yang harus dibayar setelah diskon adalah: ", biaya)
elif total < 500000 and total >= 100000:
    biaya = total-(total*(2/100))
    print("Biaya yang harus dibayar setelah diskon adalah: ", biaya)
else:
    print("Tidak ada diskon! Maka yang anda bayarkan adalah: ", total)