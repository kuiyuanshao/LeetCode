# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Transferring to python lists
        l1 = self.list_node_to_list(l1)
        l2 = self.list_node_to_list(l2)
        #Reverse the transferred python lists
        l1.reverse()
        l2.reverse()
        #Use Recursion to concat the digits
        n1 = int(self.list_to_string(l1))
        n2 = int(self.list_to_string(l2))

        #Adding the Sum into the ListNode
        sum = list(str(n1 + n2))
        for idx, digit in enumerate(str(n1 + n2)):
            if (idx == 0):
                sum[idx] = ListNode(val = digit, next = None)
            else:
                sum[idx] = ListNode(val = digit, next = sum[idx - 1])
        return sum[len(sum) - 1]

    def list_node_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def list_to_string(self, mlist):
        if len(mlist) == 0:
            return ''
        else:
            return str(mlist[0]) + '' + self.list_to_string(mlist[1:])
