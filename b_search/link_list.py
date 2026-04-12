class Node():
    def __init__(self,data):
        self.data = data
        self.next = None # link objects

    def show_list(head):
        current_node = head

        while current_node: # -> walk across node array
            print(current_node.data,end = '->')
            current_node =  current_node.next # next node

        print('Null') # after there's not node


    def lowest_value(head):
        min_value = head.data # we assume that the first lk element is the lowest
        current_node = head.next 
        while current_node:

            if current_node.data < min_value :
                min_value = current_node.data

            current_node = current_node.next # keep walk in lk
        return min_value
    
    def delete_node(head,node_to_delete):
        """to delete a node without alter lk,
        we need connect the points between the node_to_delete,
        in that way,we keep the adresses on his correct orders"""

        if head == node_to_delete: # first node deleted : first = first.next
            head = head.next 

        current_node = head
        while current_node.next and current_node.next != node_to_delete:
            current_node = current_node.next

        if current_node is None :
            return head # nothing deleted
        
        #base case : there is a target for delete
        current_node.next = current_node.next.next # we simply skip this node,so the points between it are changed

    def add_node(head,newNode,position):
        """In the same way than delete,we need to change the points of nodes between the position to connect with a new space."""

        if position == 1:
            newNode.next = head
            return newNode
        
        current_node = head
        for _ in range(position - 2):
            if current_node is None:
                break
            current_node = current_node.next # walking to the node before position
            #example : position = 2 -> node[0] (head)
        
        newNode.next = current_node.next # right point new node (head,new_node -> node2)
        current_node.next = newNode # left point new node (head->new_node->node2)

        return head
