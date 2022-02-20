
class Node:
    def __init__(self, elem):
        self.__data = elem
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        val = self.head
        while val is not None:
            print(val.get_data(), end=" ")
            val = val.get_next()
        print()

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def append_add(self, item):
        new_item = Node(item)
        if self.head is None:
            self.head = new_item
            return
        end = self.head
        while end.get_next():  # is not None
            end = end.get_next()
        end.set_next(new_item)

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def insert(self, pos, item):
        if pos > self.size():
            raise IndexError("Индекс находится за пределами списка.")
        current = self.head
        previous = None
        ind = 0
        if pos == 0:
            self.add(item)
            return
        else:
            new_item = Node(item)
            while ind < pos:
                ind += 1
                previous = current
                current = current.get_next()
            previous.set_next(new_item)
            new_item.set_next(current)

    def index(self, item):
        pos = 0
        current = self.head
        while current is not None:
            if current.get_data() == item:
                print(f"{item} находится в односвязном списке по индексу {pos}.")
                return pos
            pos += 1
            current = current.get_next()
        print(f"{item} не находится в односвязном списке.")
        return None

    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        if self.search(item):
            print(f"Удаляемое ", end="")
            index = self.index(item)
            self.pop(index)
        else:
            print(f"{item} не находится в односвязном списке.")

    def pop(self, position=None):
        ret = None
        current = self.head
        if position is None:
            ret = current.get_data()
            self.head = current.get_next()
        elif position > self.size() - 1:
            raise IndexError("Индекс находится за пределами списка.")
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.get_next()
                pos += 1
                ret = current.get_data()
            previous.set_next(current.get_next())

    def reverse(self):
        p = self.head
        self.head = None
        while p is not None:
            p0, p = p, p.get_next()
            p0.set_next(self.head)
            self.head = p0


temp = LinkedList()
temp.head = Node(93)

temp.add(31)
temp.add(77)
temp.append_add(27)
temp.append_add(54)
temp.insert(2, 17)
temp.list_print()
temp.index(64)
temp.index(17)
print(temp.search(64))
print(temp.search(17))
print(temp.size())
temp.reverse()
temp.list_print()
temp.reverse()
temp.list_print()
temp.remove(47)
temp.remove(17)
temp.list_print()
