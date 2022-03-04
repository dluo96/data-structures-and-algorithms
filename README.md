# Data Structures and Algorithms

## Introduction
### What is a data structure?
> A **data structure (DS)** is a way of organizing data so that it can be used effectively. 

### Abstract Data Type vs. Data Structure
> An **abstract data type (ADT)** is an abstraction of a data structure which provides only the interface to which a data structure must adhere to. The interface does not give any specific details about how something should be implemented or in which programming language.

Examples of ADT vs DS include:
| Abstract Data Type (ADT)      | Example Data Structures (i.e implementations) |
| ----------- | ----------- |
| List        | Dynamic Array, Linked List|
| Queue       | Linked List based Queue, Stack based Queue, Array based Queue |
| Map         | Hash Table / Hash Map, Tree Map |

Importantly, we see that each ADT can be implemented in a variety of ways. The key point is that an ADT only defines how a DS should behave and what methods it should have, **not** the implementation details of those methods. 

### Computational Complexity
Complexity analysis answers two key qustions about an algorithm:
- How much **time** does the algorithm take to finish?
- How much **space** does the algorithm need for its computation(s)?

Suppose n is the size of the input of an algorithm. I will use the following terms throughout the repo:
- Constant time: O(1)
- Logarithmic time: O(log n)
- Linear time: O(n)
- Linearithmic time: O(n log n)
- Quadratic time: O(n^2)
- Exponential time: O(b^n) where b > 1
- Factorial time: O(n!)


### Repository structure
In this repository, I cover and/or implement some important data structures:
- [x] Static Arrays and Dynamic Arrays
- [x] [Singly Linked List](singly_linked_list.py) and [Doubly Linked List](doubly_linked_list.py)
- [x] [Hash Table](hash_table.py)
- [x] [Minimum Heap](min_heap.py)
- [x] [Binary Search Tree (BST)](binary_search_tree.py)
- [x] [Stack](stack.py)
- [ ] Queue and Priority Queue
- [ ] Dequek
- [ ] Graph

I also discuss the relationship between
- Stacks and the Depth-First Search (DFS) algorithm
- Queues and the Breadth-First Search (BFS) algorithm
- Priority Queues and the A* Search algorithm

## Static Arrays and Dynamic Arrays
The array DS is important because it is used a fundamental building block of all other data structures. With arrays and pointers alone, it is possible to implement almost any DS. 

### Static Array
> A **static array** is a *fixed-length* container containing n elements that are **indexable** from `[0, 1, ..., n-1]`. 

By "indexable" we mean that the slot of each element of the static array can be referenced with an integer. It is also worth noting that:
> Static arrays are given as contiguous chunks of memory. That is, all the addresses are adjacent. 

Applications of static arrays include
- Storing and accessing sequential data
- Usage by IO routines as buffers
- Usage in dynamic programming to cache answers to subproblems

#### Time complexity
| Operation      | Static Array | Dynamic Array |
| -----------    | -----------  | ----------- |
| Access         | O(1) | O(1) |
| Search         | O(n) | O(n) |
| Insert         | N/A | O(n)  |
| Append         | N/A | O(1)  |
| Delete         | N/A | O(n)  |

Insertion, appending, and deletion don't make much sense for a static array since it has a fixed size - it cannot grow larger or smaller. 

## Dynamic Array
> A **dynamic array** can grow and shrink in size.

One way to implement a dynamic array is using a static array! These are the steps:
1. Create a static array with an initial capacity
2. Add elements to this underlying static array while keeping track of the number of elements
3. If addition of an element means that the capacity is exceeded, create a new static array with twice the capacity and copy the original elements into it. 

## Linked List
### Singly Linked List
> A **singly linked list** is a sequential list of nodes where each node has data and a pointer to another node. 

Thus, each element links to the next element, which links to the next element, and so on. The last node points to `NULL`, i.e. it has a `NULL` reference. Some key terms are:
- **Head**: the first node in a linked list.
- **Tail**: the last node in a linked list. 
- **Pointer**: a reference to another node.
- **Node**: an object containing data and a pointer

Importantly, each node in a singly linked lists holds only one pointer to the next node.

A linked list can contains pretty much any type of data including
- Strings
- Characters
- Numbers

The elements of the linked list can be unsorted or sorted. It can contain duplicate elements or all unique elements. 

Applications of linked lists include
- Some implementations of the ADTs List, Stack, and Queue
- Creating a circular list (where the pointer of the last node point to the first node)
- Implementation of hash tables that use separate **chaining** to deal with hashing **collisions**
- Implementation of adjacency lists for graphs

### Linked List vs. Array

One of the things that distinguishes a linked list from an array, which shares many of the same properties, is that the array elements are indexed. For example, you could get the fourth element via `a[3]` (constant time). In a linked list, you must start with the head and work your way through until you get to the fourth element. This takes linear time, so it's quite a bit slower. So why then would you use a linked list? The answer is that insertions and deletions can be very quick! If you want to insert an element right at the beginning of a linked list, that can be done in constant time. Likewise, if you want to delete an element from the beginning of a linked list, that also takes constant time. That is very fast. However, if you want to append an element to the end of a linked list, you have to go through the entire linked list, which takes linear time (NB: if your implementation keeps track of the tail node, appending an element is actually takes constant time). 

### Doubly Linked List
> In a **doubly linked list**, each node has two pointers, namely one reference to the next node and one reference to the previous node. 
It is similar to a singly linked list, but in addition to each element having a link to the next element, each element also links to the previous element. This can be very useful for certain operations. 

### Singly vs. Doubly Linked Lists
| Data Structure      | Advantages  | Disadvantages |
| -----------         | ----------- | ----------- |
| Singly Linked List  | Less memory, simpler implementation| Not easy to access previous elements | 
| Doubly Linked List  | Can be traversed backwards | Takes ~2x the memory |

Assuming that the implementation of the singly linked list keeps track of the head node but not the tail node, we have:
#### Time complexity
| Operation      | Singly Linked List | Doubly Linked List |
| -----------    | -----------  | ----------- |
| Search         | O(n) | O(n) |
| Insert at head | O(1) | O(1)  |
| Insert at tail | O(n) | O(1)  |
| Remove at head | O(1) | O(1)  |
| Remove at tail | O(n) | O(1)  |
| Remove in middle | O(n) | O(n)|

## Stack
> A **stack** is a one-ended linear data structure which models a real-world stack by having two operations, namely **push** and **pop**. 

A stack is a **last-in-first-out (LIFO)** data structure. Applications of stacks include:
- Undo mechanism in text editors
- Compiler syntax checking for matching braces and brackets
- Used behind the scenes to support **recursion** by keeping track of previous function calls: when a function returns, it pops the current stack frame and rewinds to the next function on the stack.
- Can be used to do a **Depth-First Search (DFS)** on a **graph**
- Tower of Hanoi: each move of a disk corresponds to a pop of its original stack and a push to its new stack

### Time complexity
The table below assumes you have implemented the stack using a linked list.
| Operation      | Stack | 
| -----------    | -----------  | 
| Push         | O(1) |
| Pop | O(1) | 
| Peek | O(1) | 
| Search | O(n) | 
| Size | O(1) |

### Implementation
A stack can be implemented in different ways including using an array, a singly linked list, or a doubly linked list. 

## Queue
> A **queue** is a linear data structure which models real-world queues by having two main operations, namely **enqueue** and **dequeue**.

A queue is a **first-in first-out (FIFO)** data structure. Note that enqueue is also known as adding or offering. Dequeue is also known as polling or removing. Applications of queues include:
- Web server request management where you want first-come first-served
- **Breadth-First Search (BFS)** for **graph traversal**

### Time complexity
| Operation      | Queue | 
| -----------    | -----------  | 
| Enqueue         | O(1) |
| Dequeue | O(1) | 
| Peek | O(1) | 
| Contains | O(n) | 
| Removal | O(n) |

### Implementation
A queue can be implemented in different ways including using an array, a singly linked list, or a doubly linked list. 

## Priority Queue
> A **priority queue (PQ)** is an abstract data type (ADT) that operates similarly to a regular queue *except each element has a priority*. The priority of the elements in the PQ determine the order in which elements are removed from the PQ. 

Note that PQs only support comparable data, i.e. the data must be able to be ordered in some way. This is necessary to ensure we can assign a priority to each element. Application of PQs include:
- A* Search in graph traversal: the PQ is used to grab the most promising node
- Any time you need to fetch the next "best" element or next "worst" element

### Priority Queue and Heap
How does a PQ know which of its element has the highest priority? Does it sort all the elements? No, it uses a heap. 
> A **heap** is a tree based DS which satisfies the **heap property**: if A is a parent node of B, then A is ordered with respect to B for all nodes A and B in the heap. 

A heap is the underlying DS for a PQ (recall that a PQ is an ADT). Though a heap is the most common implementation of a PQ, a PQ can also be implemented in other ways. 

Concretely, this means we have two types of heap:
- **Maximum Heap**: each child node is smaller than its parent node. 
- **Minimum Heap**: each child node is larger than its parent node. 

### Complexity
The table below assumes that the PQ has been implemented via a binary heap. 
| Operation      | Queue | 
| -----------    | -----------  | 
| Polling        | O(log n) |
| Peeking | O(1) | 
| Adding | O(log n)  | 
| Removing an element which isn't the root node | O(n) |
| Contains (a non-root element) | O(n) |
| Removing with the help of a hash table | O(log n) |
| Contains with the help of a hash table | O(1) |

Polling both take logarithmic time because you need to restore the heap property once you have removed the root element. Similarly, adding takes logarithmic time because you need to restore the heap property once you have added an element to the heap. Note that using a hash table will lead to a space complexity of O(n). 

## Hash Tables
At a high level, a hash table is a key-value look-up. You associate a value with every key. This leads to very fast lookups. The keys and values can basically be any type of data structure. A string is often used but it could be a class object or pretty much anything provided you have a **hash function**. At a high level, we do want to store the objects in an array. How do we go from (say) a string to a particular index in the array? That's what the hash function does. The hash function maps a string to an integer, which is later mapped to an index of the array. So we map from the key to the integer, which is then mapped to an index. We have to do the second step because the integer output of the hash function might be much larger than the size (and thus number of indexes) of the array. 

### Collisions
Note that two different keys (e.g. strings) could have the same hash code. This is because there are an infinitely many possible strings but only a finite number of hash codes. In addition, since we are remaping the hash code into an even smaller index, two keys with different hash codes can actually end up with the same index. This is called a **collision**. What do we do in this case? There are different ways to resolve collisions, one of which is called **chaining**: when there are collisions, store the associated values in a **linked list**. Thus, rather than having an array of values, we'll have an array of a linked list of values. Importantly, each linked list contains not just the values but also the original keys. 

### Runtime of a Hash Table
The time complexity of operations in a hash table depend on what assumptions we make. Most of the time, we can assume we have a good hash table with a good hash funcion which distributes our values well. For this case, the time complexity of insert, find (lookup), and delete is O(1), i.e. constant time. In the worst case scenario, the time complexity for these operations is O(n). 

## Minimum Heap

## Binary Search Tree (BST)


### Priority Queue


# References
- [Data Structures Easy to Advanced Course](https://www.youtube.com/watch?v=RBSGKlAvoiM)
