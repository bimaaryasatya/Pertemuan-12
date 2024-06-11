queue = []

# Fungsi Tambah Data Queue
def enqueue(item):
    queue.append(item)

def dequeue():
    return queue.pop(0)

def dequeue(item):
    for i,_ in enumerate(queue):
        if _ == item:
            return queue.pop(i)
    return None

def front():
    return 'Data Kosong' if len(queue) < 1 else queue[0]

def tail():
    return queue[-1]

def isempty():
    return 'Data Kosong' if len(queue) == 0 else 'Ada Data'

def isfull():
    return len(queue)

def first():
    return queue[0]

enqueue('Dimas')
enqueue('Ukin')
enqueue('Wahyu')
enqueue('Wildan')
enqueue('Kiwil')

print(f'Data pertama: {front()}')
print(f'Data terakhir: {tail()}')
print(f'Cek Data: {isempty()}')