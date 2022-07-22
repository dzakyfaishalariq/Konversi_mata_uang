import library.fungsi as fg
import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

try:
    i = 'y'
    while i == 'y':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(fg.warna_text_tebal.biru + fg.warna_text_tebal.tb_garis + '''
        ##############################################
                    Konversi Mata Uang
        ##############################################
        -> y = digunakan untuk mengulang pogram
        -> n = keluar dari pogram
            ''')
        nilai = int(input(fg.warna_text_tebal.ungu +
                    fg.warna_text_tebal.tb_garis + '> masukan nilai mata uang: $.'))
        conv = fg.conversi(nilai)
        print(fg.warna_text_tebal.ping + fg.warna_text_tebal.tb_garis +
              '> nilai mata uang: Rp. {},00'.format(conv.dolar_rupiah()))
        i = input(fg.warna_text_tebal.kuning +
                  fg.warna_text_tebal.tb_garis + '> lanjutkan (y/n): ')
    else:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(fg.warna_text_tebal.biru + fg.warna_text_tebal.tb_garis + '''
            ##############################################
                            Terima Kasih
            ##############################################
        ''')
except ValueError:
    print(fg.warna_text_tebal.merah +
          fg.warna_text_tebal.tb_garis + 'Terjadi kesalahan!!!')
