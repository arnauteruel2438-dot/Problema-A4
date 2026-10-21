LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:

    def __init__(self, cap=13):
        self._table = [[None, None, LLIURE] for _ in range(cap)]
        self._n = 0

    def _hash_function(self, key):
        return key % len(self._table)

    def _find(self, key):
        m = len(self._table)
        j = self._hash_function(key)
        for i in range(m):
            pos = (j + i) % m
            slot = self._table[pos]
            if slot[2] == LLIURE:
                return None
            if slot[2] == OCUPAT and slot[0] == key:
                return pos
        return None

    def _insert(self, key, value):
        pos = self._find(key)
        if pos is not None:                      # la clau ja hi és
            self._table[pos][1] = value
            return
        m = len(self._table)
        j = self._hash_function(key)
        for i in range(m):                       # primera posició no ocupada
            pos = (j + i) % m
            if self._table[pos][2] != OCUPAT:
                self._table[pos] = [key, value, OCUPAT]
                self._n += 1
                return

    def _resize(self, c):
        old = self._table
        self._table = [[None, None, LLIURE] for _ in range(c)]
        self._n = 0
        for slot in old:
            if slot[2] == OCUPAT:
                self._insert(slot[0], slot[1])

    def put(self, key: int, value: int) -> None:
        self._insert(key, value)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        pos = self._find(key)
        if pos is None:
            return -1
        return self._table[pos][1]

    def remove(self, key: int) -> None:
        pos = self._find(key)
        if pos is not None:
            self._table[pos] = [None, None, ESBORRAT]
            self._n -= 1

    def __len__(self):
        return self._n