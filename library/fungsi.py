class conversi:
    # pengubahan konversi mata uang
    def __init__(self, nilai):
        self.nilai = nilai

    def dolar_rupiah(self):
        rupiah = self.nilai*15024
        str_rupiah = str(rupiah)
        array = []
        for i in str_rupiah:
            array.append(i)
        array.reverse()
        a = 1
        for i in range(len(array)):
            if a % 3 == 0:
                array[a-1] = '.' + array[a-1]
            a += 1
        array[len(array) - 1] = str_rupiah[0]
        array.reverse()
        nilai = "".join(array)
        return nilai


class warna_text_tebal:
    merah = '\033[91m'
    kuning = '\033[93m'
    hijau = '\033[92m'
    biru = '\033[94m'
    ungu = '\033[95m'
    coklat = '\033[96m'
    ping = '\033[97m'
    oren = '\033[33m'
    jingga = '\033[1;33m'

    # ketebalan garis
    tb_garis = '\033[1m'
