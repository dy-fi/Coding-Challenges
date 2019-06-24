def find_middle_node(ll):
    if ll.size % 2 == 0:
        curr = head
        i = 0
        while curr:
            if i == (ll.size // 2) + 1:
                return (curr.data, curr.next.data)
    else:
        curr = head
        i = 0
        while curr:
            curr = curr.next
            i += 1
            if i == (ll.size // 2) + 1:
                return curr.data