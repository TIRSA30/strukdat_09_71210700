class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority # 1 (tertinggi), 2, 3, 4, ...

class PriorityQueueSortedList:
    def __init__(self): #konstruktor
       self._data = []
       self._size = 0


    def __len__(self): #mengembalikan ukuran Queue
        return len(self._data)

    def is_empty(self): #mengecek apakah Queue kosong ?
        return self.__len__() == 0

    #pengembalian data
    def peek(self):
        print(self._data[0])
        print()

    def add(self, x, y):
        if len(self._data):
            bantu = 0
            while self._data[bantu][1] < y:
                bantu += 1
            self._data.insert(bantu, (x, y))
        else:
            self._data.append((x, y))

    def update(self, x, y):
        coba = self._data.index((y, x))
        self._data[coba] = (y, x)

    def remove(self):
        del self._data[0]

    def removePriority(self, x):
        print("Data prioritas tertinggi: ")
        bantu = 0
        while self._data[bantu][1] != x:
            bantu += 1
        del self._data[bantu]


    def printIsiQueue(self):
        print("Isi semua Queue :")
        for i in self._data:
            print("{}," .format(i), end=" ")
        print()

    


sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
# sortedList.update(4, "Karin")
# sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()