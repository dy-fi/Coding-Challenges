def find_middle_node(ll):
    middle_index = (ll.size // 2) + 1
    if ll.size % 2 == 0:
        curr = ll.head
        i = 0
        while curr:
            if i == middle_index:
                return (curr.data, curr.next.data)
    else:
        curr = ll.head
        i = 0
        while curr:
            curr = curr.next
            i += 1
            if i == middle_index:
                return curr.data