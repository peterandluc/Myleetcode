# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    Simple linked list. Use two variables result and result_tmp to store root node is important for me,
    rank from 69% to 96%.
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = result_tmp = ListNode(0)

        while True:
            if (l1.next == None and l1.val == 0) and (l2.next == None and l2.val == 0):
                break
            tmp_0, tmp_1 = 0, 0
            tmp_0 = l1.val + l2.val + result_tmp.val
            if tmp_0 >= 10:
                tmp_0 = tmp_0 - 10
                tmp_1 = 1
            result_tmp.val = tmp_0
            result_tmp_tmp = ListNode(tmp_1)
            if l1.next == None and l2.next == None and tmp_1 == 0:
                result_tmp.next = None
            else:
                result_tmp.next = result_tmp_tmp
            result_tmp = result_tmp_tmp
            l1.val = 0
            l2.val = 0
            if l1.next != None:
                l1 = l1.next
            if l2.next != None:
                l2 = l2.next
        return result