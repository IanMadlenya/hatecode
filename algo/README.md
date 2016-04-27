Algorithm questions, usually given a real problem, and you need to figure out an optimal solution, and code it up - it is usually not bounded to any programming language.

### How to prepare
You should mimic the real interview scenario as much as possible:
* Do practice on paper - interview are usually done on paper or whiteboard, not computer.
* Do it within a limited time, like 15 minutes, or 20 minutes - as a real interview is usually time bounded, and you maybe nervous..
* Get your hands on with all following coding tactics
* Try real interviews for your non-favorite position first - the experience would be very valuable.

### Common coding tatics 
There are some useful tactics you need to be familiar with, they are very commonly used when you solve coding problems - they are patterns, they are building blocks
* recursion (how to recursive, when recursion ends?) - it could solve a lot of tree/binary related problem.
  * Fabnacci
  * binary search
* iterative(loop)
  * binary search
* bit operation (int, bitset, vector<bool>, unordered_map)
  * Count number of 1 in a integer. `a & (a-1)`
  * There is 1 interger appears once, while others all appear twice in an array, find out the sigular number. `a[0] ^ a[1] ^ a[2] ...`
* sort
  * quick sort
  * merge sort
  * bubble sort
  * selection sort
  * insert sort
* array & string
  * Operate pointers in an array -  it is always useful to maintain `pre, cur, next` pointers when you solve certain problems
    * Remove a char from a string (O(n))
    * Remove all duplicated chars from a string (O(n))
  * Operate index in an array - it is always useful to maintain `start, end` index when you solve certain problems
    * rotate index in an array: (start + 1) % 5; (start + 4) % 5; 
    * binary search
* heap (priority_queue)
  * k-way merge
* list
  * reverse a single linked list - use `pre, cur, next`
  * `slow, fast` pointers - get to the middle, check circle
* stack
  *  `isvalid('()[]{}')`
* queue
  * BFS
  * traverse a tree by level
* tree
  * LCA
  * traverse (pre-order, in-order, post-order)
    * `isValidBST(root)`
* graph: adjcent list, adjcent matrix
  * DFS
  * BFS(queue)

### Algorithm design
* Convert the problem to an known algorithm: `leetcode gas station -> max sub array -> dynamic programming`
* Divide and Conquer
* Dynamic Programming
* Greedy

### Interview tips
* Think through your solution, ask confirm questions, and dicuss it before rushing to code
* Draw some diagram to help you better analyze the solution, which could also be used to explain your idea to interviewer.
* Finish the main workflow first, and then check the edge case.
* Write your code with large interval - so you could insert code late when you see bugs
* Put `{` at the end of the previous line, rather than on a new line - you don't have enough space, like:

### Reference
* [LeetCode](https://leetcode.com)
* [LeetCode - Clean Code Handbook](https://leetcode.com/book/)
* [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/)
