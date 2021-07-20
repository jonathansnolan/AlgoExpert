# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	c = linkedList
	while c is not None:
		nd = c.next
		while nd is not None and nd.value == c.value:
			nd = nd.next
		c.next = nd
		c = nd
	return linkedList
