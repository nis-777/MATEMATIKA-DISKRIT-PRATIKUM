aktif = True
nilai_memenuhi = False
prasyarat = True

lulus_ujian = aktif and nilai_memenuhi and prasyarat

if lulus_ujian:
    print("Mahasiswa LULUS ujian")
else:
    print("Mahasiswa TIDAK LULUS ujian")
