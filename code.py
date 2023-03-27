class Codec:

    def serialize(self, root):
        # Pre-Order Traversal of Tree
        # Putting a marker to notify None/null, so we can recognize it during deserialization
        if root == None:
            return 'X,'
        
        left_subtree = self.serialize(root.left) 
        right_subtree = self.serialize(root.right)
        
        # Putting a delimiter on which we can split our string on during deserialization
        return str(root.val) + "," + left_subtree + right_subtree

    def deserializeHelper(self, data):
        # If we encounter our marker("X") for None/null node, pop out from our queue(data) and return None
        # Also its our base condition!!!
        if data[0] == "X":
            del data[0]
            return None
        
        # Making a tree node with the front most element in the queue
        new_node = TreeNode(data[0])
        del data[0] # Popping our element from queue
        
        # When we encounter one "X" we move from left subtree to current(new_node) and when we encounter
        # two "X"'s we are moving to the parent (Just trying to explain the recursion taking place)
        new_node.left = self.deserializeHelper(data) 
        new_node.right = self.deserializeHelper(data)
        
        return new_node


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Splitting our data on the delimeter we used during serialization
        data = data.split(",")
        del data[-1] # Last one will be None/null so omitting it
        return self.deserializeHelper(data)
       
