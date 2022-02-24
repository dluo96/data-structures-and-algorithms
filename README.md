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

## Hash Tables
At a high level, a hash table is a key-value look-up. You associate a value with every key. This leads to very fast lookups. The keys and values can basically be any type of data structure. A string is often used but it could be a class object or pretty much anything provided you have a **hash function**. At a high level, we do want to store the objects in an array. How do we go from (say) a string to a particular index in the array? That's what the hash function does. The hash function maps a string to an integer, which is later mapped to an index of the array. So we map from the key to the integer, which is then mapped to an index. We have to do the second step because the integer output of the hash function might be much larger than the size (and thus number of indexes) of the array. 

### Collisions
Note that two different keys (e.g. strings) could have the same hash code. This is because there are an infinitely many possible strings but only a finite number of hash codes. In addition, since we are remaping the hash code into an even smaller index, two keys with different hash codes can actually end up with the same index. This is called a **collision**. What do we do in this case? There are different ways to resolve collisions, one of which is called **chaining**: when there are collisions, store the associated values in a **linked list**. Thus, rather than having an array of values, we'll have an array of a linked list of values. Importantly, each linked list contains not just the values but also the original keys. 

### Runtime of a Hash Table
The time complexity of operations in a hash table depend on what assumptions we make. Most of the time, we can assume we have a good hash table with a good hash funcion which distributes our values well. For this case, the time complexity of insert, find (lookup), and delete is O(1), i.e. constant time. In the worst case scenario, the time complexity for these operations is O(n). 