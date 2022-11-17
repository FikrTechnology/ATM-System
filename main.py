import os


data_pemasukan = 0
data_pengeluaran = 0

def time():
    import time

    dt = time.strftime('%D %H:%M')
    return dt

def setor():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print('='*100)
    print(' '*35 + 'Selamat Datang di ATM kite')
    print('='*100)
    print('\n')

    print(' '*35 + 'Silahkan masukkan Nominal')
    inpSetor = input(' '*41+'Rp. ')
    print('\n')
    print('='*100)

    try:
        inpSetor = int(inpSetor)

        if inpSetor < 50000:
            print('Mohon Maaf, Nominal yang anda masukkan kurang dari Rp.50000')
            while True:
                inpNext = input('Ingin melanjutkan Setor Tunai? [Y/N]: ').upper()
                if inpNext == 'Y':
                    setor()
                elif inpNext == 'N':
                    show_menu()
                else:
                    print('Input yang anda masukkan Salah!!')
        elif inpSetor >= 50000 and inpSetor % 50000 == 0:
            global data_pemasukan
            data_pemasukan = int(data_pemasukan) + int(inpSetor)
            print('\n')
            print('Nominal yang anda masukkan   : Rp. ', inpSetor)
            print('Jumlah Tabungan Anda         : Rp. ', data_pemasukan)
            print('Tanggal Setor                : ', time())
            print('\n')
            print('='*100)

            while True:
                inpNext = input('Ingin melanjutkan Setor Tunai? [Y/N]: ').upper()
                if inpNext == 'Y':
                    setor()
                elif inpNext == 'N':
                    show_menu()
                else:
                    print('Input yang anda masukkan Salah!!')
        else:
            print('Input Nominal harus berkelipatan Rp.50000')
            while True:
                inpNext = input('Ingin melanjutkan Setor Tunai? [Y/N]: ').upper()
                if inpNext == 'Y':
                    setor()
                elif inpNext == 'N':
                    show_menu()
                else:
                    print('Input yang anda masukkan Salah!!')

    except ValueError:
        print('Inputan tidak sesuai')
        setor()


def tarikTunai():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print('='*100)
    print(' '*35 + 'Selamat Datang di ATM kite')
    print('='*100)
    print('\n')

    print(' '*35 + 'Silahkan masukkan Nominal')
    inpTarik = input(' '*41+'Rp. ')
    print('\n')
    print('='*100)

    try:
        inpTarik = int(inpTarik)

        if inpTarik < 50000:
            print('Mohon Maaf, Nominal yang anda masukkan kurang dari Rp.50000')
            while True:
                inpNext = input('Ingin melanjutkan Setor Tunai? [Y/N]: ').upper()
                if inpNext == 'Y':
                    setor()
                elif inpNext == 'N':
                    show_menu()
                else:
                    print('Input yang anda masukkan Salah!!')
        elif inpTarik >= 50000 and inpTarik % 50000 == 0:
            global data_pemasukan
            global data_pengeluaran
            
            if data_pemasukan >= 50000:
                if data_pemasukan >= inpTarik:
                    data_pengeluaran = int(data_pengeluaran) + int(inpTarik)
                    data_pemasukan = int(data_pemasukan) - int(inpTarik)


                    print('\n')
                    print('Nominal yang anda masukkan   : Rp. ', inpTarik)
                    print('Jumlah Tabungan Anda         : Rp. ', data_pemasukan)
                    print('Tanggal Tarik                : ', time())
                    print('\n')
                    print('='*100)

                    while True:
                        inpNext = input('Ingin melanjutkan Tarik Tunai? [Y/N]: ').upper()
                        if inpNext == 'Y':
                            tarikTunai()
                        elif inpNext == 'N':
                            show_menu()
                        else:
                            print('Input yang anda masukkan Salah!!')
                else:
                    print('\n')
                    print('Mohon Maaf Nominal anda tidak mencukupi untuk Tarik Tunai')
                    print('Tabungan anda                : Rp. ', data_pemasukan)
                    print('\n')

                    while True:
                        inpNext = input('Ingin melanjutkan Tarik Tunai? [Y/N]: ').upper()
                        if inpNext == 'Y':
                            tarikTunai()
                        elif inpNext == 'N':
                            show_menu()
                        else:
                            print('Input yang anda masukkan Salah!!')
            else:
                print('\n')
                print('Mohon Maaf Nominal anda tidak mencukupi untuk Tarik Tunai')
                print('Tabungan anda                : Rp. ', data_pemasukan)
                print('\n')

            while True:
                inpNext = input('Ingin melanjutkan Setor Tunai? [Y/N]: ').upper()
                if inpNext == 'Y':
                    setor()
                elif inpNext == 'N':
                    show_menu()
                else:
                    print('Input yang anda masukkan Salah!!')
        else:
            print('Input Nominal harus berkelipatan Rp.50000')
            while True:
                inpNext = input('Ingin melanjutkan Setor Tunai? [Y/N]: ').upper()
                if inpNext == 'Y':
                    setor()
                elif inpNext == 'N':
                    show_menu()
                else:
                    print('Input yang anda masukkan Salah!!')

    except ValueError:
        print('Inputan tidak sesuai')
        setor()


def checkSaldo():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print('='*100)
    print(' '*35 + 'Selamat Datang di ATM kite')
    print('='*100)
    print('\n')

    global data_pemasukan

    print('Tabungan Anda        : Rp. ', data_pemasukan)
    print('\n')

    while True:
        inpNext = input('Ingin melanjutkan Setor Tunai? [Y/N]: ').upper()
        if inpNext == 'Y':
            setor()
        elif inpNext == 'N':
            show_menu()
        else:
            print('Input yang anda masukkan Salah!!')


def exit():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print('='*100)
    print(' '*35 + 'Selamat Datang di ATM kite')
    print('='*100)
    print('\n')

    while True:
        inpNext = input('Ingin keluar dari ATM? [Y/N]: ').upper()
        if inpNext == 'Y':
            break
        elif inpNext == 'N':
            show_menu()
        else:
            print('Input yang anda masukkan Salah!!')


def show_menu():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print('='*100)
    print(' '*35 + 'Selamat Datang di ATM kite')
    print('='*100)
    print('\n')
    print('[1] Setor Tunai')
    print('[2] Tarik Tunai')
    print('[3] Cek Saldo')
    print('[4] Exit')
    print('\n')

    inp_menu = input('Silahkan pilih menu diatas : ')
    print('\n')

    try:
        intMenu = int(inp_menu)

        if intMenu == 1:
            setor()
        elif intMenu == 2:
            tarikTunai()
        elif intMenu == 3:
            checkSaldo()
        elif intMenu == 4:
            exit()
        else:
            print('Input yang anda masukkan tidak ada!!')
    except ValueError:
        print('Inputan tidak sesuai')
        show_menu()



if __name__ == "__main__":

    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    show_menu()