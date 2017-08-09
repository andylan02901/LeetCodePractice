 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        node1 = l1
        node2 = l2
        origNode = ListNode(0)
        nextNode = origNode
        carry = 0
        
        while node1 or node2 is not None:
            s = 0 
            if node1 is not None:
                s = s + node1.val
                node1 = node1.next
            if node2 is not None:
                s = s + node2.val
                node2 = node2.next
            s = s + carry
            nextNode.next = ListNode(s%10)
            nextNode = nextNode.next
            carry = s // 10
        if carry is 1:
            nextNode.next = ListNode(carry)
        
            
        return origNode.next
