# Merge two sorted linked list to a new sorted linked list
class ListNode:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


def merge(linkA, linkB):
    sentinelA = linkA
    sentinelB = linkB
    if not sentinelA or not sentinelB:
        return sentinelA if not sentinelB else sentinelB
    prev = None
    start = sentinelA if sentinelA.data < sentinelB.data else sentinelB
    while sentinelA and sentinelB:
        if sentinelA.data < sentinelB.data:
            prev = sentinelA
            sentinelA = sentinelA.next
        else:
            if prev:
                prev.next = sentinelB
            temp = sentinelB.next
            sentinelB.next = sentinelA
            prev = sentinelB
            sentinelB = temp
    if sentinelA:
        prev.next = sentinelA
    elif sentinelB:
        prev.next = sentinelB
    return start


def printList(n):
    pr = ""
    while n:
        pr += "[Data: {data}] -> ".format(data=n.data)
        n = n.next
    pr += "None"
    print(pr)


a = ListNode(0, ListNode(3, ListNode(8, ListNode(9, None))))
b = ListNode(1, ListNode(3, ListNode(5, ListNode(11, None))))

printList(merge(b, a))
