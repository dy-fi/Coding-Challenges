# Given a singly-linked list, find the middle value in the list.
# Example: If the given linked list is A → B → C → D → E, return C.
# Assumptions: The length (n) is odd so the linked list has a definite middle.

class Node():
    def __init__(self, val:str, next=None):
        self.val = val
        self.next = next

# for test convience
class Linked_List():
    def __init__(self, vals:[str]):
        self.head = Node(vals[0])

        last = self.head
        for i in vals[1:]:
            n = Node(i)
            last.next = n
            last = n
            
# return middle node of a linked list
def middle(ll:Linked_List) -> str:
    head = ll.head
    curr = head
    result = []    
    # traverse and get vals, curr as a read head
    while(curr):
        result.append(curr.val)
        curr = curr.next
    # return middle index
    return result[(len(result) // 2)]

# return pointer to a reversed linked list, in place
def reverse(ll:Linked_List) -> Node:
    head = ll.head
    rev = []
    curr = head

    # traverse
    while(curr):
        rev.append(curr)
        curr = curr.next

    # manually set head and head next
    ll.head = rev.pop()
    ll.head.next = rev[-1]
    # pop off stack and set next to peek
    while(rev):
        # pop off the stack
        top = rev.pop()
        # assign next to the new top of stack or None if it doesn't exist
        if rev: top.next = rev[-1]
        else: top.next = None

    return ll


if __name__ == '__main__':
    okgreen = '\033[92m'
    warn = '\033[93m'
    end = '\033[0m'

    # LINKED LIST TEST
    print(warn + "Check head of linked list" + end)

    ll = Linked_List(["a", "b", "c", "d", "e"])
    assert ll.head.val == "a"

    print(okgreen + "Linked_List tests passed!" + end)

    # MIDDLE OF LINKED LIST TESTS
    print(warn + "Check middle of str based linked list" + end)
    
    ll = Linked_List(["a", "b", "c", "d", "e"])
    assert middle(ll) == "c"

    print(okgreen + "middle() tests passed!" + end)

    # REVERSE LINKED LIST TESTS
    print(warn + "Check values of reverse linked list" + end)
    
    ll = Linked_List(["1", "2", "3", "4", "5"])
    r = reverse(ll)
    
    assert r.head.val == "5"
    assert r.head.next.val == "4"
    assert middle(r) == "3"

    print(okgreen + "reverse() tests passed!" + end)
