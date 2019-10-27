# coding:utf-8
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        """在链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node
        # 代码还可以写成下面的形式
        # node = Node(item)
        # node.next = self.__head
        # self.__head.prev = node
        # self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur  # 比单链表多的是这个

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            node = Node(item)
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            node.next = cur  # 要先处理结点，防止原来的链表断掉
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            # 最后的四句话还可以写成如下的写法
            # node.next = cur
            # node.prev = cur.prev
            # cur.prev = node
            # node.prev.next = node

    def remove(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next is not None:
                        # 判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next is not None:
                        # 判断是不是尾结点
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    dll.append(1)
    dll.travel()
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.travel()
    dll.add(100)
    dll.travel()
    dll.insert(2, 78)
    dll.travel()
    dll.insert(-1, 9)
    dll.travel()
    dll.insert(10, 11)
    dll.travel()
    print(dll.search(3))
    dll.remove(3)
    dll.travel()
    dll.remove(9)
    dll.travel()
