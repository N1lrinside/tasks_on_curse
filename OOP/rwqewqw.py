class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def __iter__(self):
        return self.val

    def __next__(self):
        if self.next:
            return self.val


User = ListNode(1)
for i in User:
    print(i, end='')
