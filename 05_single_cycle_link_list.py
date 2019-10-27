# coding:utf-8
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 考虑特殊情况包括：空链表以及只有一个结点的链表
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环cur指向尾结点，但是尾结点的元素未打印
        print(cur.elem)
        print('')

    def add(self, item):
        """在链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾结点
            node.next = self.__head
            self.__head = node
            cur.next = node
            # 最后一行或者写成
            # cur.next = self.__head

    def append(self, item):
        """在尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
            cur.next = node
            # 或者最后两行写成下面这样
            # cur.next = node
            # node.next = self.__head
            # 记住一个原则，尽量先动新添加的结点，防止链表断掉

    def insert(self, pos, item):
        # 和单链表相同
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            pre = self.__head
            node = Node(item)
            count = 0
            while count < pos-1:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        pre = None
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    # 头部结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间结点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == item:
            if pre:
                # 只有一个结点的情况
                pre.next = cur.next
            else:
                self.__head = None

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环cur指向尾结点，但是尾结点的元素未打印
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    sll = SingleCycleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.append(1)
    sll.travel()
    sll.remove(1)
    sll.travel()
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.travel()
    sll.add(100)
    sll.travel()
    sll.insert(2, 78)
    sll.travel()
    sll.insert(-1, 9)
    sll.travel()
    sll.insert(10, 11)
    sll.travel()
    print(sll.search(3))
    sll.remove(3)
    sll.travel()
    sll.remove(9)
    sll.travel()
    sll.remove(11)
    sll.travel()
