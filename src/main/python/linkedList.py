class LinkedList:

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value) + str(self.next)


def revert(list: LinkedList):
    prev = None
    current = list
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

list = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None))))
print(list)
print(revert(list))