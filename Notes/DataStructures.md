<br />

---

## **Data Structures**

---

<br />

## Arrays

<br />

*Data in order and indexed by numbered position. Stored in order in memory. Referenced by index.*

<br />

Time Complexity:
- Array elements can be references in O(1) constant time if the index is known.
- Insert/remove values at end of an array in O(1) time complexity because no values need to shift.
- Insert/remove values in the middle at worst O(n) time complexity because values will need to be shifted.

<br />

---

<br />

## Linked Lists

<br />

*Data in order. Not stored in same order in memory. Referenced by pointer from last element in list.*

<br />

Time Complexity:
- Elements have to be referenced in O(n) time complexity because you have to go through the list in order from beginning following pointers to the next value.
- Insert/remove values at the end in O(1) time complexity because no shifting occurs and pointer is deleted.
- Insert/remove values in the middle in O(1) time complexity because pointers between list elements just point to new elements instead of shifting elements.

<br />

---

<br />

## HashMaps

<br />

*Unordered data stored in key/value pairs. The key can be anything including strings. Unlike arrays where an array is ordered by ascending integers. HashMaps allow for one null key and multiple null values (unlike HashTables). They are non-synchronized across threads (unlike HashTables).*

<br />

Time Complexity:
- Insert/remove in O(1) time complexity because value is referenced by unique key and there is no order so there is no shifting.
- Search/reference values in O(1) time complexity by using the unique key.

<br />

---

<br />

## HashTables

<br />

*Unordered data stored in key/value pairs. The key can be anything including strings. Unlike arrays where an array is ordered by ascending integers. HashTables do not allow any null keys or values (unlike HashMaps). HashTables are synchronized across threads (unlike Hashmaps).*

<br />

Time Complexity:
- Insert/remove in O(1) time complexity when it is a "good" hash table (no problems like collisions).
- Search/Reference values in O(1) time complexity when it is a "good" hash table (no problems like collisions).
- "Bad" hash tables (with things like collisions) can have up to O(n) time complexity.

<br />

---

<br />

## Queues

<br />

*First in first out data structure. A doubly linked list with specific operations: add/enqueue/push and remove/dequeue/pop. Insert takes place at the rear of the list while deletion takes place at the front of the list. Each element referenced by pointers from the element before and after. Bidirectional pointers.*

<br />

Time Complexity:
- Add/remove element from front or back is O(1) time complexity since pointers start at each end.
- Searching queues can take up to O(n) time complexity because queue has to be traversed.

<br />

---

<br />

## Stacks

<br />

*Last in first out data structure. A linked list with specific operations: add/insert/push and delete/remove/pop. Insert and delete both take place on one end of the list called the top. Each element is referenced by a pointer above it (starting at the top).*

<br />

Time Complexity:
- Pushing/popping the top element in a stack is done in O(1) time complexity.
- Searching a stack is O(n) time complexity because points only go down from the top element like in a linked list.

<br />

---

<br />

## Binary Search Tree

<br />

*A tree where each node has 0-2 children. On any subtree the left nodes are less than the root node and the root node is less than all of the right nodes.*

<br />

Time Complexity:
- Insert/remove an element in O(logn) time complexity assuming a balanced tree.
- Search in O(logn) time complexity assuming a balanced tree.

<br />

---

<br />

## Heaps

<br />

*Either a min or max heap where the min or max value is the root of the tree respectively. For min trees all children will be greater. For max heap all children will be smaller. These are also always complete trees where each level is completely full except for potentially the last level. Usually layed out as an array with 0 index empty. The left child index is found with 2*i and the right child is found with 2*i + 1.*

<br />

Time Complexity:
- Find the min/max value (depending on style of heap) in O(1) time complexity.
- Insert/delete min/max value in O(logn) time complexity.

<br />

---

<br />

## Graphs

<br />

*Graphs are made up of nodes with edges that connect that node to its neighbors. These can be depicted as an adjacentcy list where each node has a coresponding list of its neighbors.*

<br />

Time Complexity:
- Time complexity of graphs varies wildly.

<br />

---