BOX_LEFT = '|'
BOX_RIGHT = '|'
BOX_TOP = '_'
BOX_BOTTOM = '_'
BOX_EDGE = '+'

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def insert_front(self, val):
        new_node = Node(val)
        new_node = self.head
        self.head = new_node


    def insert_after(self, val, key):
        curr = self.head
        while curr.val != key:
            curr = curr.next

        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node


    def insert_end(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)


    def get_width(self, val):
        width = 0
        while val != 0:
            val //= 10
            width += 1
        return width + 2


    def print_single_node(self, val):
        width = self.get_width(val)
        for i in range(width):
            print(BOX_TOP, end="")
        print()
        print(BOX_LEFT, end="")
        print(val, end="")
        print(BOX_RIGHT, end="")
        print()
        for i in range(width):
            print(BOX_BOTTOM, end="")

        print('--->', end="")


    def print_list(self):
        curr = self.head
        while curr:
            self.print_single_node(curr.val)
            curr = curr.next


    def get_height(self, val):
        pass


if __name__ == '__main__':

    llist = LinkedList()
    llist.insert_end(1)
    llist.insert_end(2)
    llist.insert_end(3)
    llist.print_list()
