q = []

def queue(i):
    q.append(i)

def call_next():
    q.pop(0)

def current() -> str:
    return q[0] if len(q) > 0 else "Tidak ada"

def next() -> str:
    return q[1] if len(q) > 1 else "Tidak ada"

print()
while True:
    print(f'Antrian Sekarang : {current()}')
    print(f'Antrian selanjutnya: {next()}')
    print('Pilihan:')
    print('1. Tambah Antrian')
    print('2. Antrian Selanjutnya')
    print('3. Lihat Antrian')
    print('4. Keluar\n\n')
    p = input('Masukkan Pilihan: ')
    if p == '1':
        n = input('Masukkan Nama: ')
        queue(n)
        print()
    elif p == '2':
        if len(q) > 0:
            call_next()
            print()
        else:
            print("Queue kosong")
    elif p == '3':
        print("Antrian: ", q)
    elif p == '4':
        break
