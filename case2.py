aktif = True
nilai_memenuhi = True
sertifikat = True

beasiswa = aktif and nilai_memenuhi and sertifikat

if beasiswa:
    print("Peserta MENDAPAT beasiswa")
else:
    print("Peserta TIDAK MENDAPAT beasiswa")
