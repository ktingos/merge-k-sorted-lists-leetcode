# define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# function that merges two sorted lists
def mergeTwoLists(l1, l2):
    start = ListNode()
    pointer = start
    
    while l1 and l2:
        if l1.val < l2.val:
            pointer.next = l1
            l1 = l1.next
        else:
            pointer.next = l2
            l2 = l2.next
        
    if not l1:
        pointer.next = l2
    else:
        pointer.next = l1
        
    return start.next