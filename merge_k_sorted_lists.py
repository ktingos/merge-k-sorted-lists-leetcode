# define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# function that converts an array to a list
def arrToList(arr):
    if len(arr) == 0:
        return None
    return ListNode(arr[0],arrToList(arr[1:]))

# function that converts a list to an array
def listToArr(l):
    if l is None:
        return []
    return [l.val] + listToArr(l.next)

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