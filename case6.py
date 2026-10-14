nilai_memenuhi = False
pengalaman = False
sertifikat = True

rekomendasi = nilai_memenuhi or pengalaman or sertifikat

if rekomendasi:
    print("Peserta MENDAPAT rekomendasi")
else:
    print("Peserta TIDAK MENDAPAT rekomendasi")
