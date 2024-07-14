# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while(fast!= None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        def rev(head):
            if head == None or head.next == None:
                return head
            newHead = rev(head.next)
            head.next.next = head
            head.next = None

            return newHead
      
        temp = rev(slow)
        
        # print(temp)
        # print(head)
        
        while(temp):
            # print(head.val)
            # print(temp.val)
            if temp.val != head.val:
                return False
           
            head = head.next
            temp = temp.next
        return True