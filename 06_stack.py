# coding:utf-8
class Stack(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)  # 对顺序表在尾部进行操作的时间复杂度是O(1)，在头部是O(N)。

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.is_empty() == []
        # return not self.is_empty()

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

