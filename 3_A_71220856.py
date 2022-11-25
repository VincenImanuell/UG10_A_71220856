nilai_1 = int(input("Masukkan nilai soal 1: "))
nilai_2 = int(input("Masukkan nilai soal 2: "))
nilai_3 = int(input("Masukkan nilai soal 3: "))
umur = int(input("Masukkan umur anda: "))

rata_nilai = (nilai_1*(50/100))+(nilai_2*(30/100))+(nilai_3*(20/100))
print("Rata-rata nilai Anda: ", rata_nilai)

if umur > 25 and rata_nilai >= 90:
    print("Selamat Anda lulus!")
elif umur <= 25 and rata_nilai >= 80:
    print("Selamat Anda lulus!")
else:
    print("Coba lagi tahun depan!")