from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def in_order(self):
        self._in_order_recursive(self.head)

    def _in_order_recursive(self, current_node):
        if not current_node:
            return
        self._in_order_recursive(current_node.left)
        print(current_node)
        self._in_order_recursive(current_node.right)

    def pre_order(self):
        self._pre_order_recursive(self.head)

    def _pre_order_recursive(self, current_node):
        if not current_node:
            return
        print(current_node)
        self._pre_order_recursive(current_node.left)
        self._pre_order_recursive(current_node.right)

    def post_order(self):
        self._post_order_recursive(self.head)

    def _post_order_recursive(self, current_node):
        if not current_node:
            return
        self._post_order_recursive(current_node.left)
        self._post_order_recursive(current_node.right)
        print(current_node)

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node:
                raise ValueError('A <Node> with that value already exists')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find(self, node_to_find: Node) -> Node:
        current_node = self.head
        while current_node:
            if node_to_find.value == current_node.value:
                return node_to_find
            elif node_to_find.value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        else:
            raise LookupError(f'{node_to_find} not found')

    def find_parent(self, node: Node) -> Node:
        if self.head and self.head.value == node.value:
            return self.head

        current_node = self.head
        while current_node:
            if(current_node.left and current_node.left.value == node.value) or \
              (current_node.right and current_node.right.value == node.value):
                return current_node
            elif node.value > current_node.value:
                current_node = current_node.right
            elif node.value < current_node.value:
                current_node = current_node.left

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, node: Node):
        to_delete = self.find(node)
        to_delete_parent = self.find_parent(node)

        if to_delete.left and to_delete.right:
            # There are 2 children nodes
            rightmost = self.find_rightmost(to_delete.left)
            rightmost_parent = self.find_parent(rightmost)

            if rightmost_parent != to_delete:
                rightmost_parent.right = rightmost.left
                rightmost.left = to_delete.left

            rightmost.right = to_delete.right

            if to_delete == to_delete_parent.left:
                to_delete_parent.left = rightmost

            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = rightmost

            else:
                self.head = rightmost

        elif to_delete.left or to_delete.right:
            # There is 1 child node
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.right or to_delete.left
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.right or to_delete.left
            else:
                self.head = to_delete.right or to_delete.left

        else:
            # No children
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = None
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None
            else:
                self.head = None
