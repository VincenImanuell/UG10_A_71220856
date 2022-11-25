input_nama = input("Masukkan nama mahasiswa : ")
input_nim = input("Masukkan NIM-nya : ")
prodi = str(input_nim[0]+input_nim[1])
angkatan = int(str(input_nim[2]+input_nim[3]))

if prodi == "71" and angkatan >= 20 and angkatan <= 22:
    print(input_nama, " merupakan mahasiswa informatika angkatan 20 hingga 22")
else:
    print(input_nama, " bukan mahasiswa informatika angkatan 20 hingga 22")