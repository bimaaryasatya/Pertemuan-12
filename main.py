from stdqueue import Standard_Queue as sq

q = sq()
c = None
print()
while True:
    print(f'Antrian Sekarang : {c if c != None else "Tidak ada"}\nAntrian selanjutnya: {q.first() if q.cur_size() > 0 else "Tidak ada"}\nPilihan:\n1. Tambah Antrian\n2. Antrian Selanjutnya\n3. Lihat Antrian\n4. Keluar\n\n')
    p = input('Masukkan Pilihan: ')
    if p == '1':
        n = input('Masukkan Nama: ')
        q.enqueue(n)
        print(f'"{n}" berhasil ditambahkan kedalam antrian')
    elif p == '2':
        if q.cur_size() > 0:
            c = q.dequeue()
            print()
        else:
            c = None
            print()
    elif p == '3':
        print("Antrian: ", q.elements)
    elif p == '4':
        break
