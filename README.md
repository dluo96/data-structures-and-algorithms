# Data Structures and Algorithms
In this repository, I implement some important data structures. 

## Linked List
A linked list is a data structure where each element links to the next element, which links to the next element, and so on. It can contains pretty much any type of data including
- Strings
- Characters
- Numbers

The elements of the linked list can be unsorted or sorted. It can contain duplicate elements or all unique elements. 

### Linked List vs. Array

One of the things that distinguishes a linked list from an array, which shares many of the same properties, is that the array elements are indexed. For example, you could get the fourth element via `a[3]` (constant time). In a linked list, you must start with the head and work your way through until you get to the fourth element. This takes linear time, so it's quite a bit slower. So why would you use a linked list? Insertions and deletions can be very quick! If you want to insert an element right at the beginning of a linked list, that can be done in constant time. Likewise, if you want to delete an element from the beginning of a linked list, that also takes constant time. That is very fast. However, if you want to append an element to the end of a linked list, you have to go through the entire linked list, which takes linear time. 

### Doubly Linked List
It is similar to a singly linked list, but in addition to each element having a link to the next element, each element also links to the previous element. This can be very useful for certain operations. 