# defining our node object
class Node(object):

    '''
        Code imported from Geeks4Geeks
    '''

    def __init__(self, data=None, next_node=None, prev_node=None):
        # our node has three properties, a piece of data, a pointer to the next node, and a pointer to the previous node.
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev


class DoubleLinkedList(object):

    def __init__(self, head=None, end=None):
        self.head = head

    def traverse(self):

        # grab the first node.
        curr_node = self.head

        # keep going until you reach the end of the list
        while curr_node != None:
            # print the piece of data and set the current node equal to the next node.
            print(curr_node.data)
            curr_node = curr_node.next_node

    def get_list_size(self):


        count = 0

        # grab the first node.
        curr_node = self.head

        # keep going until you reach the end of the list
        while curr_node != None:
            # print the piece of data and set the current node equal to the next node.
            count = count + 1
            curr_node = curr_node.next_node

        return count

    def insert_beg(self, data):

        # define a new node
        new_node = Node(data)

        # set the next node to old head
        new_node.next_node = self.head

        # because it's the head it will have no previous node.
        new_node.prev_node = None

        # handle the empty list case
        if self.head != None:
            self.head.set_prev(new_node)

        # update the head property.
        self.head = new_node

    def insert_end(self, data):

        # define a new node.
        new_node = Node(data)

        # it's at the end of our list, so there is no node after it.
        new_node.next_node = None

        # handle the empty list scenario.
        if self.head == None:
            new_node.prev_node = None
            self.head = new_node
            return

        # otherwise, grab the first node.
        first_node = self.head

        # loop to till you find the end.
        while first_node.next_node:
            first_node = first_node.next_node

        # when at the end, set the next node equal to new node.
        first_node.set_next(new_node)
        new_node.prev_node = first_node

    def insert_before(self, ref_node, data):

        if self.head is None:
            print("List is empty")
            return

            # define a new node.
        new_node = Node(data)

        # set the next node of the new node to the old node.

        # set the new_node's prev_node to the reference node's previous node
        new_node.prev_node = ref_node.prev_node

        # have the reference node pevious node point to the new node.
        ref_node.prev_node = new_node

        # have the new node's next node point to the reference node.
        new_node.next_node = ref_node

        # if it's not the head
        if new_node.prev_node != None:
            # have the ref node's old previous node now point to the new node.
            new_node.prev_node.next_node = new_node
        else:
            self.head = new_node

    def insert_after(self, ref_node, data):

        # define a new node
        new_node = Node(data)

        # have the next node of the new node equal the reference node's next node.
        new_node.next_node = ref_node.next_node

        # now point the ref node's next node point to the new node
        ref_node.next_node = new_node

        # have the new node previous node equal the reference node.
        new_node.prev_node = ref_node

        # if we aren't at the end of the list then make sure to have the node after the new node
        # point to the new node
        if new_node.next_node is not None:
            new_node.next_node.prev_node = new_node

    def reverse_list(self):

        # define two nodes, the first node and the node after the first.
        p_node = self.head
        q_node = p_node.next_node

        # take the start node and have it point to nothing (the end)
        p_node.next_node = None

        # then have it's previous node point to the q_node. (the one after the first)
        p_node.prev_node = q_node

        # keep going till the end
        while q_node is not None:
            # flip the previous with the next
            q_node.prev_node = q_node.next_node

            # have the next node point to the p_node
            q_node.next_node = p_node

            # now have the p node equal the old q node
            p_node = q_node

            # have the q node equal the old q nodes previous node.
            q_node = q_node.prev_node

        # redefine the head
        self.head = p_node

    def delete_at_start(self):

        # handle the empty list case
        if self.head is None:
            print("The list has no element to delete")
            return

            # handle the "only head" list
        if self.head.next_node is None:
            self.head = None
            return

        # have the head now equal the node after the head
        self.head = self.head.next_node

        # make sure that the head's previous node points to none
        self.head.prev_node = None

    def delete_at_end(self):

        # handle the empty list case
        if self.head is None:
            print("The list has no element to delete")
            return

        # handle the "only head" list
        if self.head.next_node is None:
            self.head = None
            return

        # grab the first node.
        curr = self.head

        # traverse till you get to the end.
        while curr.next_node is not None:
            curr = curr.next_node

        # grab the previous node of the last node and have it's next node point to nothing.
        curr.prev_node.next_node = None

    def remove_duplicates(self):

        # grab the first node and the node after the first
        previousNode = self.head
        currentNode = previousNode.next_node

        if previousNode == None:
            print("The list has no elements to delete")
            return

            # build a set to store non-duplicate values
        keys = set([previousNode.data])

        while currentNode:

            data = currentNode.data

            # if it is a duplicate
            if data in keys:

                # have the previous node's next pointer by pass the current node and point to the node after it.
                previousNode.next_node = currentNode.next_node

                # handle the situation where we aren't at the end.
                if previousNode.next_node != None:
                    # make sure to reassign the previous pointer.
                    previousNode.next_node.prev_node = previousNode

                # set up for th next loop
                currentNode = currentNode.next_node

            else:

                # in this case we found a unique value, so add it to the set.
                keys.add(data)

                # reassign the nodes
                previousNode = currentNode
                currentNode = currentNode.next_node

    def delete_element_by_value(self, x):

        # handle the empty case list
        if self.head is None:
            print("The list has no element to delete")
            return

        # handle the "only head" list
        if self.head.next_node is None:

            # check if the value matches, if it does delete node.
            if self.head.data == x:
                self.head = None
            else:
                print("Item not found")
            return

            # handle the "the first value matches" case
        if self.head.data == x:
            self.head = self.head.next_node
            self.head.prev_node = None
            return

        # grab the first node
        n = self.head

        # traverse the list
        while n.next_node is not None:

            # if the value matches
            if n.data == x:
                break

            # grab the next node
            n = n.next_node

        # handle the case that we found it in the middle of the list.
        if n.next_node is not None:

            # grab the previous node's next node and have it point to the node after the one that contains the value
            n.prev_node.next_node = n.next_node
            # grab the next node's previous node and have it point to the node before the one that contains the value
            n.next_node.prev_node = n.prev_node

        else:

            # otherwise the value is at the end.
            if n.data == x:
                # so just take the node's previous node, grab it's next node and have it point to nothing.
                n.prev_node.next_node = None
            else:
                print("Element not found")

    def rotate_list(self, k):

        # handle the case where k is less than or equal to 0
        if (k <= 0) or (k > self.get_list_size()):
            print('The K you chosen is not correct, please choose a postive k that is less than size of the list.')
            return

        # grab the head
        curr = self.head

        # traverse the list till either you reach the end or the kth element.
        count = 1
        while (count < k and curr != None):
            curr = curr.next_node
            count = count + 1

        # if kth element is none, exit.
        if curr is None:
            return

        # assign the kth element to a new variable
        kthNode = curr

        # traverse to the end of the list
        while curr.next_node is not None:
            curr = curr.next_node

        # assign the node after the last node to the original head.
        curr.next_node = self.head

        # have the original head's previous node now point to the last node.
        self.head.prev_node = curr

        # have the head now point to the node after the kth element.
        self.head = kthNode.next_node

        # have the head's previous node equal none.
        self.head.prev_node = None

        # have the node after the end of the list equal none.
        kthNode.next_node = None