# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        n= self.length(head)
        n2=n//2
        while n2>0:
            p=p.next
            n2-=1
            
        return p
            
    def length(self,head):
        p=head
        count=0
        while p:
            count+=1
            p=p.next

        return count