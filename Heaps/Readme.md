## Introduction 
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.
Mapping the elements of a heap into an array is trivial: if a node is stored at index k, then its left child is stored at index 2k + 1 and its right child at index 2k + 2 for 0 based indexing and for 1 based indexing the left child will be at 2k and right child will be at 2k + 1.

Example of Min Heap :

            5                      13
          /   \                  /    \
        10     15              16      31
       /                      /  \     /  \
     30                     41    51  100  41


## Min Heap Representation
How is Min Heap represented ?
A Min Heap is a Complete Binary Tree. A Min heap is typically represented as an array. The root element will be at Arr[0]. For any ith node, i.e., Arr[i]:

```commandline
Arr[(i // 2] returns its parent node.
Arr[(2 * i) + 1] returns its left child node.
Arr[(2 * i) + 2] returns its right child node.
```

## Heap Operations 
Operations on Heap:
getMin(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).
extractMin(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Log n) as
              this operation needs to maintain the heap property (by calling heapify()) after removing root.
insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree.
          If new key is larger than its parent, then we don’t need to do anything. Otherwise,
          we need to traverse up to fix the violated heap property.


Heap is an elegant data structure that is commonly used for Priority Queue implementation.

Binary-Heap implementation, which means that a node can have at most two children. In a min-heap,
a node dominates its children by having a smaller key than they do,
while in a max-heap parent nodes dominate by being bigger.

