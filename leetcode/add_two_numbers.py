
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def traverse_linked_list(self, ll):
        items = ""
        while (ll):
            items += str(ll.val)
            ll = ll.next
        return int(items[::-1])
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = self.traverse_linked_list(l1) + self.traverse_linked_list(l2)
    
        
        head = ListNode(0)
        result = head
        
        for num in str(sum)[::-1]:
            result.next = ListNode(num)
            result = result.next
        
        return head.next
            