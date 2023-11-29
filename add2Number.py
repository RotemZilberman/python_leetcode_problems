# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reversedLists(self, l1):
        if l1.next == None:
            return l1
        l2 = self.reversedLists(l1.next)
        l1.next.next = l1
        l1.next = None
        return l2

    def createNumber(self, l1):
        number = 0
        while l1 != None:
            number = number * 10 + l1.val
            l1 = l1.next
        return number

    def createList(self, number):
        if number < 10:
            return ListNode(number)
        ls = ListNode(number % 10)
        l2 = self.createList(number / 10)
        ls.next = l2
        return ls

    def addTwoNumbers(self, l1, l2):
        number = self.reversedLists(l1).self.createNumber(l1) + self.reversedLists(l2).self.createNumber(l2)
        return self.createList(number)


