# Date: 02/05/2024
# Level order Traversal of a Tree



#For your reference:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def level_order(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    return_list = []
    queue = [root]
    while queue:
        temp_list = []
        for i in range(len(queue)):
            node = queue.pop(0)
            temp_list.append(node.value)
            if node.children is not None:
                for j in node.children:
                    queue.append(j)
        return_list.append(temp_list)

    return return_list
