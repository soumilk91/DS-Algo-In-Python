"""
At DoorDash, menus are updated daily even hourly to keep them up-to-date. Each menu can be regarded as a tree.
When the merchant sends us the latest menu, can we calculate
how many nodes have changed/added/deleted?


Assume each Node structure is as below:

class Node {
        String key;
        int value;
        List children;
}
Assume there are no duplicate nodes with the same key.
Output: Return the number of changed nodes in the tree.
Existing tree
               a(1)
            /
         b(2)      c(3)
        /     \
      d(4)    e(5)      f(6)

New tree
            a(1)

               c(3)

                   f(66)

a(1) a is the key, 1 is the value
For example, there are a total of 4 changed nodes. Node b, Node d, Node e are automatically set to inactive.
The value of Node f changed as well.


Existing tree
            a(1)
          /
        b(2)      c(3)
      /       \
  d(4)      e(5)      g(7)
New tree
                a(1)
            /
         b(2)         h(8)
      /    |   \
e(5)   d(4)   f(6)       g(7)


There are a total of 5 changed nodes. Node f is a newly-added node. c(3) and old g(7) are deactivated and h(8) and
g(7) are newly added nodes
followup print out the changes
"""


class Node:
    def __init__(self, key, value, children=None):
        self.key = key
        self.value = value
        self.children = children if children else []


# Function to build a map of tree nodes
def build_node_map(node, node_map):
    if not node:
        return
    node_map[node.key] = node
    for child in node.children:
        build_node_map(child, node_map)
    return



# Function to compare two trees
def compare_trees(old_root, new_root):
    old_node_map = {}
    new_node_map = {}

    # Build maps for both old and new trees
    build_node_map(old_root, old_node_map)
    build_node_map(new_root, new_node_map)

    changed_count = 0

    # Check for deleted and changed nodes
    for old_key, old_node in old_node_map.items():
        if old_key not in new_node_map:
            print(f"Node {old_key} is deleted.")
            changed_count += 1
        elif old_node.value != new_node_map[old_key].value:
            print(f"Node {old_key} has changed value from {old_node.value} to {new_node_map[old_key].value}.")
            changed_count += 1

    # Check for added nodes
    for new_key, new_node in new_node_map.items():
        if new_key not in old_node_map:
            print(f"Node {new_key} is added with value {new_node.value}.")
            changed_count += 1

    return changed_count
