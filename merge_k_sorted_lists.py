"""Solution for the merge k sorted lists problem on leetcode"""


class ListNode:
    """ListNode class"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def arr_to_list(arr):
    """converts an array to a list"""
    if len(arr) == 0:
        return None
    return ListNode(arr[0], arr_to_list(arr[1:]))


def list_to_arr(lst):
    """converts a list to an array"""
    if lst is None:
        return []
    return [lst.val] + list_to_arr(lst.next)


def merge_two_lists(lst1, lst2):
    """merges two sorted lists"""
    start = ListNode()
    pointer = start

    while lst1 and lst2:
        if lst1.val < lst2.val:
            pointer.next = list1
            lst1 = lst1.next
        else:
            pointer.next = list2
            lst2 = lst2.next
        pointer = pointer.next

    if not list1:
        pointer.next = lst2
    else:
        pointer.next = lst1

    return start.next


list1 = arr_to_list([1, 4, 5])
list2 = arr_to_list([1, 3, 4])
list3 = arr_to_list([2, 6])

print(list_to_arr(merge_two_lists(list1, list2)))
